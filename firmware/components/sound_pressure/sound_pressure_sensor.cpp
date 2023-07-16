#include "sound_pressure_sensor.h"

#include "esphome.h"
#include <cmath>

namespace esphome {
namespace sound_pressure {

#define REFERENCE_SOUND_PRESSURE 94.0f // dB

static const char *const TAG = "sound_pressure";

void SoundPressureSensor::dump_config() {
  LOG_SENSOR("", "Sound Pressure Sensor", this);
  ESP_LOGCONFIG(TAG, "  Sample Duration: %.2fs", this->sample_duration_ / 1e3f);
  ESP_LOGCONFIG(TAG, "  Sensitivity: %.2f", this->mic_sensitivity_);
  ESP_LOGCONFIG(TAG, "  Amplifier Gain: %.2f", this->amp_gain_);
  ESP_LOGCONFIG(TAG, "  DC Bias: %.2f", this->dc_bias_);
  ESP_LOGCONFIG(TAG, "  Refernce Voltage: '%s'", this->reference_voltage_);
  LOG_UPDATE_INTERVAL(this);
}

void SoundPressureSensor::setup() {
  // Calculate reference voltage from mic sensitivity
  this->reference_voltage_ = pow(10, this->mic_sensitivity_ / 20);
}

void SoundPressureSensor::update() {
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
    const float result = 20 * log10(rms / this->reference_voltage_)
      + REFERENCE_SOUND_PRESSURE 
      //- this->mic_sensitivity_ 
      - this->amp_gain_;

    ESP_LOGD(TAG, "'%s' - RMS: %.6fV, Sound Pressure: %.3fdb", this->name_.c_str(), rms, result);
    this->publish_state(result);
  });

  this->last_value_ = 0.0;
  this->is_sampling_ = true;
  this->num_samples_ = 0;
  this->squared_sum_ = 0.0f;
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

  this->num_samples_++;
  
  float volts = value - this->dc_bias_;
  this->squared_sum_ += volts * volts;
}

}  // namespace sound_pressure
}  // namespace esphome
