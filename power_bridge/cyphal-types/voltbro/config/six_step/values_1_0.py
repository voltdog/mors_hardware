# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/mors_ws/src/mors_hardware/power_bridge/cyphal-types/voltbro/config/six_step/values.1.0.dsdl
#
# Generated at:  2024-04-08 11:06:00.231510 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.config.six_step.values
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.primitive.scalar
import voltbro.config.six_step


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class values_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 predict_change:    None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 detect_stall:      None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 encoder_filtering: None | uavcan.primitive.scalar.Real32_1_0 = None,
                 speed_filtering:   None | uavcan.primitive.scalar.Real32_1_0 = None,
                 sampling_interval: None | uavcan.primitive.scalar.Real32_1_0 = None,
                 stall_timeout:     None | uavcan.primitive.scalar.Real32_1_0 = None,
                 stall_tolerance:   None | uavcan.primitive.scalar.Real32_1_0 = None,
                 current_limit:     None | uavcan.primitive.scalar.Real32_1_0 = None,
                 speed_mult:        None | uavcan.primitive.scalar.Real32_1_0 = None,
                 I_mult:            None | uavcan.primitive.scalar.Real32_1_0 = None,
                 PWM_mult:          None | uavcan.primitive.scalar.Real32_1_0 = None,
                 max_PWM_per_s:     None | uavcan.primitive.scalar.Integer32_1_0 = None,
                 speed_const:       None | uavcan.primitive.scalar.Real32_1_0 = None,
                 torque_const:      None | uavcan.primitive.scalar.Real32_1_0 = None,
                 max_current:       None | uavcan.primitive.scalar.Real32_1_0 = None,
                 stall_current:     None | uavcan.primitive.scalar.Real32_1_0 = None,
                 velocity_pid:      None | voltbro.config.six_step.pid_config_1_0 = None,
                 current_pid:       None | voltbro.config.six_step.pid_config_1_0 = None) -> None:
        """
        voltbro.config.six_step.values.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param predict_change:    uavcan.primitive.scalar.Integer8.1.0 predict_change
        :param detect_stall:      uavcan.primitive.scalar.Integer8.1.0 detect_stall
        :param encoder_filtering: uavcan.primitive.scalar.Real32.1.0 encoder_filtering
        :param speed_filtering:   uavcan.primitive.scalar.Real32.1.0 speed_filtering
        :param sampling_interval: uavcan.primitive.scalar.Real32.1.0 sampling_interval
        :param stall_timeout:     uavcan.primitive.scalar.Real32.1.0 stall_timeout
        :param stall_tolerance:   uavcan.primitive.scalar.Real32.1.0 stall_tolerance
        :param current_limit:     uavcan.primitive.scalar.Real32.1.0 current_limit
        :param speed_mult:        uavcan.primitive.scalar.Real32.1.0 speed_mult
        :param I_mult:            uavcan.primitive.scalar.Real32.1.0 I_mult
        :param PWM_mult:          uavcan.primitive.scalar.Real32.1.0 PWM_mult
        :param max_PWM_per_s:     uavcan.primitive.scalar.Integer32.1.0 max_PWM_per_s
        :param speed_const:       uavcan.primitive.scalar.Real32.1.0 speed_const
        :param torque_const:      uavcan.primitive.scalar.Real32.1.0 torque_const
        :param max_current:       uavcan.primitive.scalar.Real32.1.0 max_current
        :param stall_current:     uavcan.primitive.scalar.Real32.1.0 stall_current
        :param velocity_pid:      voltbro.config.six_step.pid_config.1.0 velocity_pid
        :param current_pid:       voltbro.config.six_step.pid_config.1.0 current_pid
        """
        self._predict_change:    uavcan.primitive.scalar.Integer8_1_0
        self._detect_stall:      uavcan.primitive.scalar.Integer8_1_0
        self._encoder_filtering: uavcan.primitive.scalar.Real32_1_0
        self._speed_filtering:   uavcan.primitive.scalar.Real32_1_0
        self._sampling_interval: uavcan.primitive.scalar.Real32_1_0
        self._stall_timeout:     uavcan.primitive.scalar.Real32_1_0
        self._stall_tolerance:   uavcan.primitive.scalar.Real32_1_0
        self._current_limit:     uavcan.primitive.scalar.Real32_1_0
        self._speed_mult:        uavcan.primitive.scalar.Real32_1_0
        self._I_mult:            uavcan.primitive.scalar.Real32_1_0
        self._PWM_mult:          uavcan.primitive.scalar.Real32_1_0
        self._max_PWM_per_s:     uavcan.primitive.scalar.Integer32_1_0
        self._speed_const:       uavcan.primitive.scalar.Real32_1_0
        self._torque_const:      uavcan.primitive.scalar.Real32_1_0
        self._max_current:       uavcan.primitive.scalar.Real32_1_0
        self._stall_current:     uavcan.primitive.scalar.Real32_1_0
        self._velocity_pid:      voltbro.config.six_step.pid_config_1_0
        self._current_pid:       voltbro.config.six_step.pid_config_1_0

        if predict_change is None:
            self.predict_change = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(predict_change, uavcan.primitive.scalar.Integer8_1_0):
            self.predict_change = predict_change
        else:
            raise ValueError(f'predict_change: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(predict_change).__name__}')

        if detect_stall is None:
            self.detect_stall = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(detect_stall, uavcan.primitive.scalar.Integer8_1_0):
            self.detect_stall = detect_stall
        else:
            raise ValueError(f'detect_stall: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(detect_stall).__name__}')

        if encoder_filtering is None:
            self.encoder_filtering = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(encoder_filtering, uavcan.primitive.scalar.Real32_1_0):
            self.encoder_filtering = encoder_filtering
        else:
            raise ValueError(f'encoder_filtering: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(encoder_filtering).__name__}')

        if speed_filtering is None:
            self.speed_filtering = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(speed_filtering, uavcan.primitive.scalar.Real32_1_0):
            self.speed_filtering = speed_filtering
        else:
            raise ValueError(f'speed_filtering: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(speed_filtering).__name__}')

        if sampling_interval is None:
            self.sampling_interval = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(sampling_interval, uavcan.primitive.scalar.Real32_1_0):
            self.sampling_interval = sampling_interval
        else:
            raise ValueError(f'sampling_interval: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(sampling_interval).__name__}')

        if stall_timeout is None:
            self.stall_timeout = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(stall_timeout, uavcan.primitive.scalar.Real32_1_0):
            self.stall_timeout = stall_timeout
        else:
            raise ValueError(f'stall_timeout: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(stall_timeout).__name__}')

        if stall_tolerance is None:
            self.stall_tolerance = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(stall_tolerance, uavcan.primitive.scalar.Real32_1_0):
            self.stall_tolerance = stall_tolerance
        else:
            raise ValueError(f'stall_tolerance: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(stall_tolerance).__name__}')

        if current_limit is None:
            self.current_limit = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(current_limit, uavcan.primitive.scalar.Real32_1_0):
            self.current_limit = current_limit
        else:
            raise ValueError(f'current_limit: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(current_limit).__name__}')

        if speed_mult is None:
            self.speed_mult = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(speed_mult, uavcan.primitive.scalar.Real32_1_0):
            self.speed_mult = speed_mult
        else:
            raise ValueError(f'speed_mult: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(speed_mult).__name__}')

        if I_mult is None:
            self.I_mult = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(I_mult, uavcan.primitive.scalar.Real32_1_0):
            self.I_mult = I_mult
        else:
            raise ValueError(f'I_mult: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(I_mult).__name__}')

        if PWM_mult is None:
            self.PWM_mult = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(PWM_mult, uavcan.primitive.scalar.Real32_1_0):
            self.PWM_mult = PWM_mult
        else:
            raise ValueError(f'PWM_mult: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(PWM_mult).__name__}')

        if max_PWM_per_s is None:
            self.max_PWM_per_s = uavcan.primitive.scalar.Integer32_1_0()
        elif isinstance(max_PWM_per_s, uavcan.primitive.scalar.Integer32_1_0):
            self.max_PWM_per_s = max_PWM_per_s
        else:
            raise ValueError(f'max_PWM_per_s: expected uavcan.primitive.scalar.Integer32_1_0 '
                             f'got {type(max_PWM_per_s).__name__}')

        if speed_const is None:
            self.speed_const = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(speed_const, uavcan.primitive.scalar.Real32_1_0):
            self.speed_const = speed_const
        else:
            raise ValueError(f'speed_const: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(speed_const).__name__}')

        if torque_const is None:
            self.torque_const = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(torque_const, uavcan.primitive.scalar.Real32_1_0):
            self.torque_const = torque_const
        else:
            raise ValueError(f'torque_const: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(torque_const).__name__}')

        if max_current is None:
            self.max_current = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(max_current, uavcan.primitive.scalar.Real32_1_0):
            self.max_current = max_current
        else:
            raise ValueError(f'max_current: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(max_current).__name__}')

        if stall_current is None:
            self.stall_current = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(stall_current, uavcan.primitive.scalar.Real32_1_0):
            self.stall_current = stall_current
        else:
            raise ValueError(f'stall_current: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(stall_current).__name__}')

        if velocity_pid is None:
            self.velocity_pid = voltbro.config.six_step.pid_config_1_0()
        elif isinstance(velocity_pid, voltbro.config.six_step.pid_config_1_0):
            self.velocity_pid = velocity_pid
        else:
            raise ValueError(f'velocity_pid: expected voltbro.config.six_step.pid_config_1_0 '
                             f'got {type(velocity_pid).__name__}')

        if current_pid is None:
            self.current_pid = voltbro.config.six_step.pid_config_1_0()
        elif isinstance(current_pid, voltbro.config.six_step.pid_config_1_0):
            self.current_pid = current_pid
        else:
            raise ValueError(f'current_pid: expected voltbro.config.six_step.pid_config_1_0 '
                             f'got {type(current_pid).__name__}')

    @property
    def predict_change(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 predict_change
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._predict_change

    @predict_change.setter
    def predict_change(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._predict_change = x
        else:
            raise ValueError(f'predict_change: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def detect_stall(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 detect_stall
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._detect_stall

    @detect_stall.setter
    def detect_stall(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._detect_stall = x
        else:
            raise ValueError(f'detect_stall: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def encoder_filtering(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 encoder_filtering
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._encoder_filtering

    @encoder_filtering.setter
    def encoder_filtering(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._encoder_filtering = x
        else:
            raise ValueError(f'encoder_filtering: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def speed_filtering(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 speed_filtering
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._speed_filtering

    @speed_filtering.setter
    def speed_filtering(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._speed_filtering = x
        else:
            raise ValueError(f'speed_filtering: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def sampling_interval(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 sampling_interval
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._sampling_interval

    @sampling_interval.setter
    def sampling_interval(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._sampling_interval = x
        else:
            raise ValueError(f'sampling_interval: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def stall_timeout(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 stall_timeout
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._stall_timeout

    @stall_timeout.setter
    def stall_timeout(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._stall_timeout = x
        else:
            raise ValueError(f'stall_timeout: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def stall_tolerance(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 stall_tolerance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._stall_tolerance

    @stall_tolerance.setter
    def stall_tolerance(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._stall_tolerance = x
        else:
            raise ValueError(f'stall_tolerance: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def current_limit(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 current_limit
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._current_limit

    @current_limit.setter
    def current_limit(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._current_limit = x
        else:
            raise ValueError(f'current_limit: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def speed_mult(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 speed_mult
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._speed_mult

    @speed_mult.setter
    def speed_mult(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._speed_mult = x
        else:
            raise ValueError(f'speed_mult: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def I_mult(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 I_mult
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._I_mult

    @I_mult.setter
    def I_mult(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._I_mult = x
        else:
            raise ValueError(f'I_mult: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def PWM_mult(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 PWM_mult
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._PWM_mult

    @PWM_mult.setter
    def PWM_mult(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._PWM_mult = x
        else:
            raise ValueError(f'PWM_mult: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def max_PWM_per_s(self) -> uavcan.primitive.scalar.Integer32_1_0:
        """
        uavcan.primitive.scalar.Integer32.1.0 max_PWM_per_s
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._max_PWM_per_s

    @max_PWM_per_s.setter
    def max_PWM_per_s(self, x: uavcan.primitive.scalar.Integer32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer32_1_0):
            self._max_PWM_per_s = x
        else:
            raise ValueError(f'max_PWM_per_s: expected uavcan.primitive.scalar.Integer32_1_0 got {type(x).__name__}')

    @property
    def speed_const(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 speed_const
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._speed_const

    @speed_const.setter
    def speed_const(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._speed_const = x
        else:
            raise ValueError(f'speed_const: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def torque_const(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 torque_const
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._torque_const

    @torque_const.setter
    def torque_const(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._torque_const = x
        else:
            raise ValueError(f'torque_const: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def max_current(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 max_current
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._max_current

    @max_current.setter
    def max_current(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._max_current = x
        else:
            raise ValueError(f'max_current: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def stall_current(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 stall_current
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._stall_current

    @stall_current.setter
    def stall_current(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._stall_current = x
        else:
            raise ValueError(f'stall_current: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def velocity_pid(self) -> voltbro.config.six_step.pid_config_1_0:
        """
        voltbro.config.six_step.pid_config.1.0 velocity_pid
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity_pid

    @velocity_pid.setter
    def velocity_pid(self, x: voltbro.config.six_step.pid_config_1_0) -> None:
        if isinstance(x, voltbro.config.six_step.pid_config_1_0):
            self._velocity_pid = x
        else:
            raise ValueError(f'velocity_pid: expected voltbro.config.six_step.pid_config_1_0 got {type(x).__name__}')

    @property
    def current_pid(self) -> voltbro.config.six_step.pid_config_1_0:
        """
        voltbro.config.six_step.pid_config.1.0 current_pid
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._current_pid

    @current_pid.setter
    def current_pid(self, x: voltbro.config.six_step.pid_config_1_0) -> None:
        if isinstance(x, voltbro.config.six_step.pid_config_1_0):
            self._current_pid = x
        else:
            raise ValueError(f'current_pid: expected voltbro.config.six_step.pid_config_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.predict_change._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.detect_stall._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.encoder_filtering._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.speed_filtering._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.sampling_interval._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.stall_timeout._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.stall_tolerance._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.current_limit._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.speed_mult._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.I_mult._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.PWM_mult._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.max_PWM_per_s._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.speed_const._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.torque_const._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.max_current._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.stall_current._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        # Delimited serialization of voltbro.config.six_step.pid_config.1.0, fixed bit length 320 (40 bytes)
        _ser_.add_aligned_u32(40)  # Delimiter header is constant in this case.
        _ser_base_offset_ = _ser_.current_bit_length
        self.velocity_pid._serialize_(_ser_)
        assert _ser_.current_bit_length - _ser_base_offset_ == 320
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        # Delimited serialization of voltbro.config.six_step.pid_config.1.0, fixed bit length 320 (40 bytes)
        _ser_.add_aligned_u32(40)  # Delimiter header is constant in this case.
        _ser_base_offset_ = _ser_.current_bit_length
        self.current_pid._serialize_(_ser_)
        assert _ser_.current_bit_length - _ser_base_offset_ == 320
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 528 <= (_ser_.current_bit_length - _base_offset_) <= 1168, \
            'Bad serialization of voltbro.config.six_step.values.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> values_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "predict_change"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "detect_stall"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "encoder_filtering"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "speed_filtering"
        _des_.pad_to_alignment(8)
        _f3_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f4_ holds the value of "sampling_interval"
        _des_.pad_to_alignment(8)
        _f4_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f5_ holds the value of "stall_timeout"
        _des_.pad_to_alignment(8)
        _f5_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f6_ holds the value of "stall_tolerance"
        _des_.pad_to_alignment(8)
        _f6_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f7_ holds the value of "current_limit"
        _des_.pad_to_alignment(8)
        _f7_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f8_ holds the value of "speed_mult"
        _des_.pad_to_alignment(8)
        _f8_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f9_ holds the value of "I_mult"
        _des_.pad_to_alignment(8)
        _f9_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f10_ holds the value of "PWM_mult"
        _des_.pad_to_alignment(8)
        _f10_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f11_ holds the value of "max_PWM_per_s"
        _des_.pad_to_alignment(8)
        _f11_ = uavcan.primitive.scalar.Integer32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f12_ holds the value of "speed_const"
        _des_.pad_to_alignment(8)
        _f12_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f13_ holds the value of "torque_const"
        _des_.pad_to_alignment(8)
        _f13_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f14_ holds the value of "max_current"
        _des_.pad_to_alignment(8)
        _f14_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f15_ holds the value of "stall_current"
        _des_.pad_to_alignment(8)
        _f15_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f16_ holds the value of "velocity_pid"
        _des_.pad_to_alignment(8)
        # Delimited deserialization of voltbro.config.six_step.pid_config.1.0, extent 320
        _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
        if _dh_ * 8 > _des_.remaining_bit_length:
            raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                    f'but the remaining length is only {_des_.remaining_bit_length} bits')
        _nested_ = _des_.fork_bytes(_dh_)
        _des_.skip_bits(_dh_ * 8)
        _f16_ = voltbro.config.six_step.pid_config_1_0._deserialize_(_nested_)
        del _nested_
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f17_ holds the value of "current_pid"
        _des_.pad_to_alignment(8)
        # Delimited deserialization of voltbro.config.six_step.pid_config.1.0, extent 320
        _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
        if _dh_ * 8 > _des_.remaining_bit_length:
            raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                    f'but the remaining length is only {_des_.remaining_bit_length} bits')
        _nested_ = _des_.fork_bytes(_dh_)
        _des_.skip_bits(_dh_ * 8)
        _f17_ = voltbro.config.six_step.pid_config_1_0._deserialize_(_nested_)
        del _nested_
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = values_1_0(
            predict_change=_f0_,
            detect_stall=_f1_,
            encoder_filtering=_f2_,
            speed_filtering=_f3_,
            sampling_interval=_f4_,
            stall_timeout=_f5_,
            stall_tolerance=_f6_,
            current_limit=_f7_,
            speed_mult=_f8_,
            I_mult=_f9_,
            PWM_mult=_f10_,
            max_PWM_per_s=_f11_,
            speed_const=_f12_,
            torque_const=_f13_,
            max_current=_f14_,
            stall_current=_f15_,
            velocity_pid=_f16_,
            current_pid=_f17_)
        _des_.pad_to_alignment(8)
        assert 528 <= (_des_.consumed_bit_length - _base_offset_) <= 1168, \
            'Bad deserialization of voltbro.config.six_step.values.1.0'
        assert isinstance(self, values_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'predict_change=%s' % self.predict_change,
            'detect_stall=%s' % self.detect_stall,
            'encoder_filtering=%s' % self.encoder_filtering,
            'speed_filtering=%s' % self.speed_filtering,
            'sampling_interval=%s' % self.sampling_interval,
            'stall_timeout=%s' % self.stall_timeout,
            'stall_tolerance=%s' % self.stall_tolerance,
            'current_limit=%s' % self.current_limit,
            'speed_mult=%s' % self.speed_mult,
            'I_mult=%s' % self.I_mult,
            'PWM_mult=%s' % self.PWM_mult,
            'max_PWM_per_s=%s' % self.max_PWM_per_s,
            'speed_const=%s' % self.speed_const,
            'torque_const=%s' % self.torque_const,
            'max_current=%s' % self.max_current,
            'stall_current=%s' % self.stall_current,
            'velocity_pid=%s' % self.velocity_pid,
            'current_pid=%s' % self.current_pid,
        ])
        return f'voltbro.config.six_step.values.1.0({_o_0_})'

    _EXTENT_BYTES_ = 146

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8n9mbt0{`t;TWlO>6<#Nfy}l)OLk$s9>wwg{mu%;LDL2zV+OpW)IHe$HG@YIKvuC!mGt;>^cBP{9fvS;4)J>+M0#Sje;1Nr_'
        '@l;WPsHh-3AXM?h8;^bjQ32<l8Sk!VW;ZQCv=5Es*?-RY&i|kP+$UEiUwQIWE&UhY>Ft<-X*aZh_?B*4&+2WPG&IBQd2V2ZB#9Tk'
        'L~N^vOY`v^k0jTVd!A38OIG74&2k*#Cs2zQE`)w$gpp4ULyl>V-oq{K*mCW#?Yj-bbuL+*Mqq7gK}fvDmTpHRNaDJ-Mf|{W9lG1}'
        '6Z!gj(wu14UPzu#;yFzZL*HsgA;K@>)+6-pqmua8Ig8llK$%(1)I(hhsfI9}5n(o7iS#W)cN(5gFKKO&Mquc+?l&HFLee3=lE6G1'
        'KTrggE+%k$F8qm6TJ-ly;-w2#$026E*<tg{X>BXiY~pl6NSbxj(9nZW>$xUscsgEg9c)9z8fTHWPFZM{+IN!8B>os0QFlz;H-|TR'
        'F>2$rj-{qe;z`YPjU=umQCp8s4p~ua?_}P2E`c*}XMoz6#Pf-vqo<Rr@p0{vwM|UTbNx`W%w!{8(gHW~4T21tXr7K|#nbf1w%SQN'
        ')53V!Zc*xWyxYVBcs97y`;!q`2cbRJ546kZ?W2K@DlMe%fZAWyeT2<>?q%X@ZQn9G_*y61A@LpEPU25`QQNi*%_p76rs@qmiMvf@'
        '4nz%x%s!Pl5$%8A#s=G98q`@yNNsl#PY&=BK5;_oy)DZi$yI2;18B0gjr-np;M;+15f~QVQSpbY@T=+j1$@oD8z0qNFNs%1Z4&JC'
        '+AdxSHCZP;7b7Rckblf0z8<>%aF!WhVHm?>@rjmhnwHZkf#7k<-H2?w@lKJ8J7l5oQnK2t?*?s5HZR)<V=ijrb$gaW!w(nwHeF29'
        '5JXE;=~<0zd%Bb6<3`jD+G%th$3QVHBShtN2fan@hKzn<z$paHn<ONN!63EmGGvf~cZ^EGO`_X8HzolwOJ>g5t{xsrEV!$=0(ZlG'
        'aQ};_e^2i?Rv2O8#50$C-Jo`+CFfkeMzQ#AUSK$d;{{3L6_HaEQB_!0W&~E@1w{~9N##UAU=o^l!}$e`So-odZe;JQ_%wY2j3-(I'
        'R;(=Uf(KW=b%vE>S>{;j{+0U<mKSM40)xr-ZFnXC?keybAb`9I3aIcPd<H%XpM%fC7hny(2oJ&8_(W!n!*L7`r!fnUKr_8NY{2<`'
        'P(0CJeKTWTq%p99F#sBMJv@bW(($j2JagdPCE^%ZXndOJn1eJ@O5S@KaVG+gU^3nWwG`+*&qlUJP2!{7s&NZxoM@rdBW@IqIx)kz'
        'HU_z4kP$l>k)P&u+PA7PvzhL_$Q}WhdUOo4-un9b2=*YXPv4}ojF0S3mty&F+|gsR0Qv>|{5=KGZT)lq4>7cWwM3&<!g8bq)mEI#'
        'e1JniFv8CBSje7<$T-LxJt%kh*uWZzIg+oA4f*a<qb3&5N)<+0$$6{qzqm=lxDW{YA+VN*09=M=zadW4YOJivlFGAKog|KDMVV1p'
        'LF8nC<7J)}E?$&mRbgZXe??AI1VL3LtZFJN3$mmzREConSz)m7iM%39jHsxhs7O2~OOhfhtjvl6BTy<YvI4Jgf`r=(Jje2!q$n!B'
        'vI>F~0gu2xh8KC6mP$op@HCbYWl0oStgDPHae^qQ45Ko<qVgOH3yh41DI$aARb+Wy#l7iiJjY9j;y6wf6jl-yMiE7o$5S~TZ;MyN'
        't1FzuVR04&8845@@~ExMDvZjioT@4c%ZUu?&TtZ|2rMTkxUZyCRd43z)tkHbUXjPro&FB$_TS*I@4aqI!Y$|A+HlUTVa}};b8gDh'
        'Iy(09QiT77GOck;a}4vg)EK^QYsB|mpH|gs;7qYD6Kbec_&dA<|Ac?Qzu?{O1O_ksyE}<L-6QyjMw&35H+DSG?KAnDH=U;>PBeJ}'
        '#`S}=#3^c!nE#cf&kv1Kx1V(#ItDwHGg&;7jbvC%=$FX&-MY(o$MmIp3RfQ#et$&Zz&;5m^$Jq245$a-0yzi2fz&t3-~u@Vuh%9('
        'r;j4M%*X}SD1EI$pvcIA9{z*{^v_xOeFtOgT?{T7SGN>;-6@KhrjI&(%+SXyK86Acr)2ttf(-?gikI=@Df>$HH6S`2p0W?k)A7l#'
        ';q*M}8!&J0_cSMHZOWQ_Risw<xzvw`L-^yHbS~c{9to{c9~Mt%^M0|;&~Jp)p|!rfn{~>l?FOmgvnar>zy4GOH?KwWTf}w^E8NjA'
        'G0WxRkF;|ijA;Wz?ll6-0B{Mu3l_W#FF^v=;Ct{2d>>wgAHomdNAMc_1bz%Zh1cO%@H6-|ya~UB-@xzSE%-gW-R)3M|DoHZZiDyj'
        '>G(wU-x9Z0M?NH({}KKp{D&F8+3z29>>u?(+272{%py`3%gv@hejx)hNM*|40yzh_klHGP3*;P(g9!eWzy)#+-bLze8C)Re;60@7'
        'mB9sa4!(iZ8)a~ToP+m~x?ctt$QgKjk#^U`ind!~<N^$(GZg|Q#xFC07Nxf;1WJtj1dr0a3V{+M7ucor-3oycBNy1C^t}p!5+fJ5'
        'LFqRt1d5FAc{+onGW)4Lj+SMLj3JrDBUItZ3U3q``4BXRL(pP21TACVw6JGh!+!ZH_R80=Pri;l@=ffIZ^7Hx7GW?ReXxzTYabq|'
        'x)0+!-md!yWq#$Le&j<^cY_}GznPG_Pxd$OYPf7(8#e@H_8v6^?M+q>L5=?adQfgnXBhwh'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)