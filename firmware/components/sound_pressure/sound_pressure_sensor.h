#pragma once

#include "esphome/core/component.h"
#include "esphome/core/hal.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/voltage_sampler/voltage_sampler.h"

namespace esphome {
namespace sound_pressure {

class SoundPressureSensor : public sensor::Sensor, public PollingComponent {
 public:
  void update() override;
  void loop() override;
  void dump_config() override;
  float get_setup_priority() const override {
    // After the base sensor has been initialized
    return setup_priority::DATA - 1.0f;
  }

  void set_sample_duration(uint32_t sample_duration) { sample_duration_ = sample_duration; }
  void set_source(voltage_sampler::VoltageSampler *source) { source_ = source; }
  void set_amp_gain(float amp_gain) { amp_gain_ = amp_gain; }
  void set_vcc_factor(float vcc_factor) { vcc_factor_ = vcc_factor; }
  void set_dc_bias(float dc_bias) { dc_bias_ = dc_bias; }
  void set_mic_sensitivity(int mic_sensitivity) { mic_sensitivity_ = mic_sensitivity; }

 protected:
  /// High Frequency loop() requester used during sampling phase.
  HighFrequencyLoopRequester high_freq_;

  /// Duration in ms of the sampling phase.
  uint32_t sample_duration_;
  /// The sampling source to read values from.
  voltage_sampler::VoltageSampler *source_;
  /// The gain applied to the source.
  float amp_gain_;
  /// The DC bias applied to the source.
  float dc_bias_;
  /// The factor to apply to the RMS results to get back to VCC levels.
  float vcc_factor_;
  /// The sensitivity of the microphone in dBV/Pa.
  int mic_sensitivity_;

  float last_value_ = 0.0f;
  bool is_sampling_ = false;
  int num_samples_ = 0;
  float squared_sum_ = 0.0f;

  float reference_voltage_;
};

}  // namespace sound_pressure
}  // namespace esphome
