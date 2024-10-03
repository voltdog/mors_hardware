# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/mors_ws/src/mors_hardware/power_bridge/cyphal-types/voltbro/config/six_step/log_item.1.0.dsdl
#
# Generated at:  2024-04-08 11:06:00.211747 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.config.six_step.log_item
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
class log_item_1_0:
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
                 is_on:           None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 is_stalling:     None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 target_speed:    None | uavcan.primitive.scalar.Real32_1_0 = None,
                 speed:           None | uavcan.primitive.scalar.Real32_1_0 = None,
                 elec_theta:      None | uavcan.primitive.scalar.Real32_1_0 = None,
                 PWM:             None | uavcan.primitive.scalar.Integer32_1_0 = None,
                 I_A:             None | uavcan.primitive.scalar.Real32_1_0 = None,
                 I_B:             None | uavcan.primitive.scalar.Real32_1_0 = None,
                 I_C:             None | uavcan.primitive.scalar.Real32_1_0 = None,
                 velocity_report: None | voltbro.config.six_step.pid_report_1_0 = None,
                 current_report:  None | voltbro.config.six_step.pid_report_1_0 = None) -> None:
        """
        voltbro.config.six_step.log_item.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param is_on:           uavcan.primitive.scalar.Integer8.1.0 is_on
        :param is_stalling:     uavcan.primitive.scalar.Integer8.1.0 is_stalling
        :param target_speed:    uavcan.primitive.scalar.Real32.1.0 target_speed
        :param speed:           uavcan.primitive.scalar.Real32.1.0 speed
        :param elec_theta:      uavcan.primitive.scalar.Real32.1.0 elec_theta
        :param PWM:             uavcan.primitive.scalar.Integer32.1.0 PWM
        :param I_A:             uavcan.primitive.scalar.Real32.1.0 I_A
        :param I_B:             uavcan.primitive.scalar.Real32.1.0 I_B
        :param I_C:             uavcan.primitive.scalar.Real32.1.0 I_C
        :param velocity_report: voltbro.config.six_step.pid_report.1.0 velocity_report
        :param current_report:  voltbro.config.six_step.pid_report.1.0 current_report
        """
        self._is_on:           uavcan.primitive.scalar.Integer8_1_0
        self._is_stalling:     uavcan.primitive.scalar.Integer8_1_0
        self._target_speed:    uavcan.primitive.scalar.Real32_1_0
        self._speed:           uavcan.primitive.scalar.Real32_1_0
        self._elec_theta:      uavcan.primitive.scalar.Real32_1_0
        self._PWM:             uavcan.primitive.scalar.Integer32_1_0
        self._I_A:             uavcan.primitive.scalar.Real32_1_0
        self._I_B:             uavcan.primitive.scalar.Real32_1_0
        self._I_C:             uavcan.primitive.scalar.Real32_1_0
        self._velocity_report: voltbro.config.six_step.pid_report_1_0
        self._current_report:  voltbro.config.six_step.pid_report_1_0

        if is_on is None:
            self.is_on = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(is_on, uavcan.primitive.scalar.Integer8_1_0):
            self.is_on = is_on
        else:
            raise ValueError(f'is_on: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(is_on).__name__}')

        if is_stalling is None:
            self.is_stalling = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(is_stalling, uavcan.primitive.scalar.Integer8_1_0):
            self.is_stalling = is_stalling
        else:
            raise ValueError(f'is_stalling: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(is_stalling).__name__}')

        if target_speed is None:
            self.target_speed = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(target_speed, uavcan.primitive.scalar.Real32_1_0):
            self.target_speed = target_speed
        else:
            raise ValueError(f'target_speed: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(target_speed).__name__}')

        if speed is None:
            self.speed = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(speed, uavcan.primitive.scalar.Real32_1_0):
            self.speed = speed
        else:
            raise ValueError(f'speed: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(speed).__name__}')

        if elec_theta is None:
            self.elec_theta = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(elec_theta, uavcan.primitive.scalar.Real32_1_0):
            self.elec_theta = elec_theta
        else:
            raise ValueError(f'elec_theta: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(elec_theta).__name__}')

        if PWM is None:
            self.PWM = uavcan.primitive.scalar.Integer32_1_0()
        elif isinstance(PWM, uavcan.primitive.scalar.Integer32_1_0):
            self.PWM = PWM
        else:
            raise ValueError(f'PWM: expected uavcan.primitive.scalar.Integer32_1_0 '
                             f'got {type(PWM).__name__}')

        if I_A is None:
            self.I_A = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(I_A, uavcan.primitive.scalar.Real32_1_0):
            self.I_A = I_A
        else:
            raise ValueError(f'I_A: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(I_A).__name__}')

        if I_B is None:
            self.I_B = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(I_B, uavcan.primitive.scalar.Real32_1_0):
            self.I_B = I_B
        else:
            raise ValueError(f'I_B: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(I_B).__name__}')

        if I_C is None:
            self.I_C = uavcan.primitive.scalar.Real32_1_0()
        elif isinstance(I_C, uavcan.primitive.scalar.Real32_1_0):
            self.I_C = I_C
        else:
            raise ValueError(f'I_C: expected uavcan.primitive.scalar.Real32_1_0 '
                             f'got {type(I_C).__name__}')

        if velocity_report is None:
            self.velocity_report = voltbro.config.six_step.pid_report_1_0()
        elif isinstance(velocity_report, voltbro.config.six_step.pid_report_1_0):
            self.velocity_report = velocity_report
        else:
            raise ValueError(f'velocity_report: expected voltbro.config.six_step.pid_report_1_0 '
                             f'got {type(velocity_report).__name__}')

        if current_report is None:
            self.current_report = voltbro.config.six_step.pid_report_1_0()
        elif isinstance(current_report, voltbro.config.six_step.pid_report_1_0):
            self.current_report = current_report
        else:
            raise ValueError(f'current_report: expected voltbro.config.six_step.pid_report_1_0 '
                             f'got {type(current_report).__name__}')

    @property
    def is_on(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 is_on
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._is_on

    @is_on.setter
    def is_on(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._is_on = x
        else:
            raise ValueError(f'is_on: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def is_stalling(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 is_stalling
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._is_stalling

    @is_stalling.setter
    def is_stalling(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._is_stalling = x
        else:
            raise ValueError(f'is_stalling: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def target_speed(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 target_speed
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._target_speed

    @target_speed.setter
    def target_speed(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._target_speed = x
        else:
            raise ValueError(f'target_speed: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def speed(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 speed
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._speed

    @speed.setter
    def speed(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._speed = x
        else:
            raise ValueError(f'speed: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def elec_theta(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 elec_theta
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._elec_theta

    @elec_theta.setter
    def elec_theta(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._elec_theta = x
        else:
            raise ValueError(f'elec_theta: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def PWM(self) -> uavcan.primitive.scalar.Integer32_1_0:
        """
        uavcan.primitive.scalar.Integer32.1.0 PWM
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._PWM

    @PWM.setter
    def PWM(self, x: uavcan.primitive.scalar.Integer32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer32_1_0):
            self._PWM = x
        else:
            raise ValueError(f'PWM: expected uavcan.primitive.scalar.Integer32_1_0 got {type(x).__name__}')

    @property
    def I_A(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 I_A
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._I_A

    @I_A.setter
    def I_A(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._I_A = x
        else:
            raise ValueError(f'I_A: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def I_B(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 I_B
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._I_B

    @I_B.setter
    def I_B(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._I_B = x
        else:
            raise ValueError(f'I_B: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def I_C(self) -> uavcan.primitive.scalar.Real32_1_0:
        """
        uavcan.primitive.scalar.Real32.1.0 I_C
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._I_C

    @I_C.setter
    def I_C(self, x: uavcan.primitive.scalar.Real32_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real32_1_0):
            self._I_C = x
        else:
            raise ValueError(f'I_C: expected uavcan.primitive.scalar.Real32_1_0 got {type(x).__name__}')

    @property
    def velocity_report(self) -> voltbro.config.six_step.pid_report_1_0:
        """
        voltbro.config.six_step.pid_report.1.0 velocity_report
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity_report

    @velocity_report.setter
    def velocity_report(self, x: voltbro.config.six_step.pid_report_1_0) -> None:
        if isinstance(x, voltbro.config.six_step.pid_report_1_0):
            self._velocity_report = x
        else:
            raise ValueError(f'velocity_report: expected voltbro.config.six_step.pid_report_1_0 got {type(x).__name__}')

    @property
    def current_report(self) -> voltbro.config.six_step.pid_report_1_0:
        """
        voltbro.config.six_step.pid_report.1.0 current_report
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._current_report

    @current_report.setter
    def current_report(self, x: voltbro.config.six_step.pid_report_1_0) -> None:
        if isinstance(x, voltbro.config.six_step.pid_report_1_0):
            self._current_report = x
        else:
            raise ValueError(f'current_report: expected voltbro.config.six_step.pid_report_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.is_on._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.is_stalling._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.target_speed._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.speed._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.elec_theta._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.PWM._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.I_A._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.I_B._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.I_C._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        # Delimited serialization of voltbro.config.six_step.pid_report.1.0, fixed bit length 128 (16 bytes)
        _ser_.add_aligned_u32(16)  # Delimiter header is constant in this case.
        _ser_base_offset_ = _ser_.current_bit_length
        self.velocity_report._serialize_(_ser_)
        assert _ser_.current_bit_length - _ser_base_offset_ == 128
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        # Delimited serialization of voltbro.config.six_step.pid_report.1.0, fixed bit length 128 (16 bytes)
        _ser_.add_aligned_u32(16)  # Delimiter header is constant in this case.
        _ser_base_offset_ = _ser_.current_bit_length
        self.current_report._serialize_(_ser_)
        assert _ser_.current_bit_length - _ser_base_offset_ == 128
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 304 <= (_ser_.current_bit_length - _base_offset_) <= 560, \
            'Bad serialization of voltbro.config.six_step.log_item.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> log_item_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "is_on"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "is_stalling"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "target_speed"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "speed"
        _des_.pad_to_alignment(8)
        _f3_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f4_ holds the value of "elec_theta"
        _des_.pad_to_alignment(8)
        _f4_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f5_ holds the value of "PWM"
        _des_.pad_to_alignment(8)
        _f5_ = uavcan.primitive.scalar.Integer32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f6_ holds the value of "I_A"
        _des_.pad_to_alignment(8)
        _f6_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f7_ holds the value of "I_B"
        _des_.pad_to_alignment(8)
        _f7_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f8_ holds the value of "I_C"
        _des_.pad_to_alignment(8)
        _f8_ = uavcan.primitive.scalar.Real32_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f9_ holds the value of "velocity_report"
        _des_.pad_to_alignment(8)
        # Delimited deserialization of voltbro.config.six_step.pid_report.1.0, extent 128
        _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
        if _dh_ * 8 > _des_.remaining_bit_length:
            raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                    f'but the remaining length is only {_des_.remaining_bit_length} bits')
        _nested_ = _des_.fork_bytes(_dh_)
        _des_.skip_bits(_dh_ * 8)
        _f9_ = voltbro.config.six_step.pid_report_1_0._deserialize_(_nested_)
        del _nested_
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f10_ holds the value of "current_report"
        _des_.pad_to_alignment(8)
        # Delimited deserialization of voltbro.config.six_step.pid_report.1.0, extent 128
        _dh_ = _des_.fetch_aligned_u32()  # Read the delimiter header.
        if _dh_ * 8 > _des_.remaining_bit_length:
            raise _des_.FormatError(f'Delimiter header specifies {_dh_ * 8} bits, '
                                    f'but the remaining length is only {_des_.remaining_bit_length} bits')
        _nested_ = _des_.fork_bytes(_dh_)
        _des_.skip_bits(_dh_ * 8)
        _f10_ = voltbro.config.six_step.pid_report_1_0._deserialize_(_nested_)
        del _nested_
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = log_item_1_0(
            is_on=_f0_,
            is_stalling=_f1_,
            target_speed=_f2_,
            speed=_f3_,
            elec_theta=_f4_,
            PWM=_f5_,
            I_A=_f6_,
            I_B=_f7_,
            I_C=_f8_,
            velocity_report=_f9_,
            current_report=_f10_)
        _des_.pad_to_alignment(8)
        assert 304 <= (_des_.consumed_bit_length - _base_offset_) <= 560, \
            'Bad deserialization of voltbro.config.six_step.log_item.1.0'
        assert isinstance(self, log_item_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'is_on=%s' % self.is_on,
            'is_stalling=%s' % self.is_stalling,
            'target_speed=%s' % self.target_speed,
            'speed=%s' % self.speed,
            'elec_theta=%s' % self.elec_theta,
            'PWM=%s' % self.PWM,
            'I_A=%s' % self.I_A,
            'I_B=%s' % self.I_B,
            'I_C=%s' % self.I_C,
            'velocity_report=%s' % self.velocity_report,
            'current_report=%s' % self.current_report,
        ])
        return f'voltbro.config.six_step.log_item.1.0({_o_0_})'

    _EXTENT_BYTES_ = 70

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8n9mbt0{`t-O^h7H6`u9q&U*c`#=(FPFa`l@jEDa3YJL|R3}~{;vIc^PtWI@zd0r1a-A(_jcacEm0K!rW7P~n{3O9~Mi9jF@'
        'QG{~J0Vzk0K@mSWaE!zyucmu`c6w*+#7dL{Bh7U6d#_%-dhdN-)m+&1!QF>zy-#*WxbDP`*EC}mxzuxCqn5{-rX6&{Aa)a$XZxRE'
        'p4-Kt^Za_q^2_<LH}lu?`D~Br`aX+tsAc=lBvEQ7X~Z_0>^6PcMHh|Lz)P$sXxf2)&TThicg>6w7B;=0ZKCIHp4H7&7R7GhbAQt>'
        'mgCELYpPXyJAX6JW=)zTk!z(1i}SPSd_v>{t32C%+GU<I3}>(D(1e-^j}fK|A?(c>DP6Ux-wY$ZO?Q<wW1D(3YChv9tj!{l!#+6B'
        '4+IXK&Edv!^39W?82HMwLucH!&z#cP<^;`}mYbL!^V<pJtvW_%(>O7^frAkq&5kVh-SBD6Q>a_yDoji5t$ZcVet~JEzC$Bt)X_Vs'
        'h1=S_O1%`<-(@<1ooBT?wP<#DB#WlCUexFH98SO;F-GICFk&{vTIUzD1Liq*jX7o*M2YD-`BHYsjDs|?87e$xh7{MzruoBjtvs7q'
        '#*SHA=F-c!x2XqkZ3uY%ccqveH0=gaY@UzvY-b!{Nc(&5fYG0)5t{7_gYzsht;luS_*!Rc35$H{<=L%aYI&}0My#EBJiK8g(c7M)'
        'fEd9@+V>Pi#QgWm*c6*WlNT#bc<v74$}w&tVt&G_x9Zv~zX(lu08?gp==Yv}ZHKu<!({v&13&2|zwEuA!Pm07*-kSEvG*rAiPyVU'
        'fSbZd7FjpI&PlN4pAA_=lOP(!nGG(sF+7_cT&9lW`t6DlJkPaDsfRmWAJ?LXq7~lD=UerS*g~*{g(K{_)WYp{U7xof4(J*mO!F4R'
        'O!L`$O|}+NzlX=A)QYX5yWH61V8wLd`v4Dc3+iT3hkfaJe1(d|5O}vw0^SOvo-AzxJH*D!X)mD3COE-8tp?l+$Kn2WFzPOC`)-mV'
        'T(X&S5w&@Cv8eUa<rt@B_sWVO5lL1wO(v>Dh-wf~)CEN(vO*M9)C@^g6d~tm8$}f~GwsPWbmXl!A`Y4uyNE--;TGK%KiK&72~pE^'
        'T@tnX8^`;@vmAyXAmrYFS7VSag1iI@=<`6pfCu3rco-gmN8vG8fXCq^oXQRs+1T8@@Kmo;;b~~~_6|$%+@KX+9E@HrlxKP68(4WT'
        'dBNc~m?w%~3w6%0ruz~awHbmTWJmy&!o9+`zm0A$^O$WWz!JJ$)sJ3<ZnrP|U6oRAE(>3_$nS^n+iS}24TE+62PxjU{Hw*Sv$yjZ'
        '^YMwAlM^+ks+t|;X!l6c@0@f3hpvOH$|=5*_4$7vw3@PA?UF(57RuVed3fz5b*feqbwk$-Swz%nk}RsaKtx5AbVZVNnFCT*HQgYB'
        'F5pv@RH7(`p&?ogQCD=02z-vD2|5uF(5g&yO;CxUszj3|UDJq8L|s%BLE%za6&0CCiiYkLSrTPQBgDX0k)SbAa0&bhvMTGG0*EHy'
        'YNDX(nyQM(7lN)yimDibU<fiXWC<rLf{u$3RY2NMMOik`H(yPbWDTt(Niq~7YAO+ksv0t`D#^H8+#+tBNScJCqbNFV9)p!JT3sZ9'
        'AsUil5F$#dfUygbCK5%I6oP&=vK1={S7#;ZzWY=eDXI4y^3h-6FW1gTnsVJ>Sr`S&0)k~>94rTVQAgA>Srp-UR_XLVqtTuiuUB|S'
        'D3pwEWgh+pU&7zvn{?uSvVHb?2-G`KULmGSeBfbOAOsJJK1T3>9-`zw+V*oJr}T}d0-xWo{4J0BY^FHv@lwJsxm$YsdP3IVYZi0q'
        '1(aSGO8dr}#YKwYj|kU46=44ozPZ-y!ME@od=EdsKSq*(mj-@e^OL-FAv=Os$>Lu_WCEiOK8kDi(d_UGemwC;T=M#{))epUg59@F'
        '?mr9BPdxGp1&`+YrWNY9*$N9;;!e6?y;9tJ=Egdd-<5i)tMyaYs&jd5Bktv}NH^#C-&K`m4<B4*USPY)`haD}oA?Xf>2@0R?xCBE'
        '%5pF`0s!aWU2x%jcn@;81Xth#_&t0KpTHmBGx)SKj~oi0caGzua}0m3Uc2m2|IgQTw)AKvezyF7vRoNpzm7dxA5y|f(YbRdovRYX'
        'nE36&SU{;zH69a}#>*&Ot{RVtOJn3={8o&|#2*#L8z|kV8jp!f&sR`-rD{ATE{(rJ=~q?bF>z`9BT9d)8gCYNZa^gV>=);zfG%!K'
        'Rc2HaBXb0<5_VMQj4MhmpG7X8E4cg!(uIpuaS3VSW2A^rksCNI{8t&Ja{|pqD5O)zcZ{<$!+p%+&nU-t4)O)Am*6|M4cvAbIBcEX'
        'hQrI8O(5~b<sDnIc=KNg-^foe6951'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)