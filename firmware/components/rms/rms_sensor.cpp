#include "rms_sensor.h"

#include "esphome.h"
#include <cmath>

namespace esphome {
namespace rms {

static const char *const TAG = "sound_pressure";

void RMSSensor::dump_config() {
  LOG_SENSOR("", "RMS Sensor", this);
  ESP_LOGCONFIG(TAG, "  Sample Duration: %.2fs", this->sample_duration_ / 1e3f);
  ESP_LOGCONFIG(TAG, "  DC Bias: %.2f", this->dc_bias_);
  LOG_UPDATE_INTERVAL(this);
}

void RMSSensor::update() {
  // Update only starts the sampling phase, in loop() the actual sampling is happening.

  // Request a high loop() execution interval during sampling phase.
  this->high_freq_.start();

  // Set timeout for ending sampling phase
  this->set_timeout("read", this->sample_duration_, [this]() {
    this->is_sampling_ = false;
    this->high_freq_.stop();

    if (this->num_samples_ == 0 || this->squared_sum_ == 0.0f) {
      ESP_LOGW(TAG, "'%s' - No valid samples found", this->name_.c_str());
      return;
    }

    const float rms = sqrt(this->squared_sum_ / this->num_samples_);
    this->publish_state(rms);
  });

  this->is_sampling_ = true;
  this->num_samples_ = 0;
  this->squared_sum_ = 0.0f;
}

void RMSSensor::loop() {
  if (!this->is_sampling_)
    return;

  // Perform a single sample
  float value = this->source_->sample();
  if (std::isnan(value))
    return;

  this->num_samples_++;
  
  float volts = value - this->dc_bias_;
  this->squared_sum_ += volts * volts;
}

}  // namespace sound_pressure
}  // namespace esphome
