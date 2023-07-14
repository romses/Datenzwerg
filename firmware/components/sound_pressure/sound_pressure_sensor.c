#include "sound_pressure_sensor.h"

#include "esphome/core/log.h"
#include <cmath>

namespace esphome {
namespace sound_pressure {

static const char *const TAG = "sound_pressure";
static const int PA_TO_DB = 94;

void SoundPressureSensor::dump_config() {
  LOG_SENSOR("", "Sound Pressure Sensor", this);
  ESP_LOGCONFIG(TAG, "  Sample Duration: %.2fs", this->sample_duration_ / 1e3f);
  ESP_LOGCONFIG(TAG, "  Sensitivity: %.2f", this->mic_sensitivity_);
  ESP_LOGCONFIG(TAG, "  Amplifier Gain: %.2f", this->amp_gain_);
  LOG_UPDATE_INTERVAL(this);
}

void SoundPressureSensor::setup() {
  // Calculate transfer factor from mic sensitivity
  this->transfer_factor_ = pow(10, this->mic_sensitivity_ / 20);
}

void SoundPressureSensor::update() {
  // Update only starts the sampling phase, in loop() the actual sampling is happening.

  // Request a high loop() execution interval during sampling phase.
  this->high_freq_.start();

  // Set timeout for ending sampling phase
  this->set_timeout("read", this->sample_duration_, [this]() {
    this->is_sampling_ = false;
    this->high_freq_.stop();

    const float peak_to_peak = this->max_value_ - this->min_value_;
    const float rms = peak_to_peak * 0.707;
    const float result = log10(rms / this->transfer_factor_) * 20 + PA_TO_DB + this->sensitivity_ - this->amp_gain_;

    ESP_LOGD(TAG, "'%s' - Peak to peak: %.3fV, RMS: %.3fV, Sound Pressure: %.3fdb", this->name_.c_str(), peak_to_peak, rms, result);
    this->publish_state(result);
  });

  this->last_value_ = 0.0;
  this->min_value_ = 1000.0f;
  this->max_value_ = -1000.0f;
  this->is_sampling_ = true;
}

void SoundPressureSensor::loop() {
  if (!this->is_sampling_)
    return;

  // Perform a single sample
  float value = this->source_->sample();
  if (std::isnan(value))
    return;

  // Assuming a sine wave, avoid requesting values faster than the ADC can provide them
  if (this->last_value_ == value)
    return;
  this->last_value_ = value;

  if (value < this->min_value_) {
    this->min_value_ = value;
    ESP_LOGD(TAG, "'%s' - New min value: %.3fA", this->name_.c_str(), this->min_value_);
  }

  if (value > this->max_value_) {
    this->max_value_ = value;
    ESP_LOGD(TAG, "'%s' - New max value: %.3fA", this->name_.c_str(), this->max_value_);
  }
}

}  // namespace sound_pressure
}  // namespace esphome
