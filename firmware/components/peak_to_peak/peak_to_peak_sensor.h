#pragma once

#include "esphome/core/component.h"
#include "esphome/core/hal.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/voltage_sampler/voltage_sampler.h"

namespace esphome {
namespace peak_to_peak {

class PeakToPeakSensor : public sensor::Sensor, public PollingComponent {
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

 protected:
  /// High Frequency loop() requester used during sampling phase.
  HighFrequencyLoopRequester high_freq_;

  /// Duration in ms of the sampling phase.
  uint32_t sample_duration_;
  /// The sampling source to read values from.
  voltage_sampler::VoltageSampler *source_;

  bool is_sampling_ = false;
  float min_value_ = 1000.0f;
  float max_value_ = -1000.0f;
};

}  // namespace peak_to_peak
}  // namespace esphome
