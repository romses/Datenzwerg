#include "peak_to_peak_sensor.h"

#include "esphome.h"
#include <cmath>

namespace esphome {
namespace peak_to_peak {

static const char *const TAG = "peak_to_peak";

void PeakToPeakSensor::dump_config() {
  LOG_SENSOR("", "PeakToPeak Sensor", this);
  ESP_LOGCONFIG(TAG, "  Sample Duration: %.2fs", this->sample_duration_ / 1e3f);
  LOG_UPDATE_INTERVAL(this);
}

void PeakToPeakSensor::update() {
  // Update only starts the sampling phase, in loop() the actual sampling is happening.

  // Request a high loop() execution interval during sampling phase.
  this->high_freq_.start();

  // Set timeout for ending sampling phase
  this->set_timeout("read", this->sample_duration_, [this]() {
    this->is_sampling_ = false;
    this->high_freq_.stop();

    if (this->min_value_ == 1000.0f || this->max_value_ == -1000.0f) {
      ESP_LOGW(TAG, "'%s' - No valid samples found", this->name_.c_str());
      return;
    }

    this->publish_state(this->max_value_ - this->min_value_);
  });

  this->is_sampling_ = true;
  this->min_value_ = 1000.0f;
  this->max_value_ = -1000.0f;
}

void PeakToPeakSensor::loop() {
  if (!this->is_sampling_)
    return;

  // Perform a single sample
  float value = this->source_->sample();
  if (std::isnan(value))
    return;

  if (value < this->min_value_) {
    this->min_value_ = value;
  }

  if (value > this->max_value_) {
    this->max_value_ = value;
  }
}

}  // namespace peak_to_peak
}  // namespace esphome
