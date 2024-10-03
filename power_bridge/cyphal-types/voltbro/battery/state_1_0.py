# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/mors_ws/src/mors_hardware/power_bridge/cyphal-types/voltbro/battery/state.1.0.dsdl
#
# Generated at:  2024-04-08 11:06:00.264493 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.battery.state
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.primitive
import uavcan.primitive.scalar
import uavcan.si.unit.electric_charge
import uavcan.si.unit.electric_current
import uavcan.si.unit.voltage


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class state_1_0:
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
                 voltage:                 None | uavcan.si.unit.voltage.Scalar_1_0 = None,
                 current:                 None | uavcan.si.unit.electric_current.Scalar_1_0 = None,
                 charge:                  None | uavcan.si.unit.electric_charge.Scalar_1_0 = None,
                 capacity:                None | uavcan.si.unit.electric_charge.Scalar_1_0 = None,
                 design_capacity:         None | uavcan.si.unit.electric_charge.Scalar_1_0 = None,
                 power_supply_status:     None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 power_supply_health:     None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 power_supply_technology: None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 is_present:              None | uavcan.primitive.scalar.Integer8_1_0 = None,
                 location:                None | uavcan.primitive.String_1_0 = None,
                 serial_number:           None | uavcan.primitive.String_1_0 = None) -> None:
        """
        voltbro.battery.state.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param voltage:                 uavcan.si.unit.voltage.Scalar.1.0 voltage
        :param current:                 uavcan.si.unit.electric_current.Scalar.1.0 current
        :param charge:                  uavcan.si.unit.electric_charge.Scalar.1.0 charge
        :param capacity:                uavcan.si.unit.electric_charge.Scalar.1.0 capacity
        :param design_capacity:         uavcan.si.unit.electric_charge.Scalar.1.0 design_capacity
        :param power_supply_status:     uavcan.primitive.scalar.Integer8.1.0 power_supply_status
        :param power_supply_health:     uavcan.primitive.scalar.Integer8.1.0 power_supply_health
        :param power_supply_technology: uavcan.primitive.scalar.Integer8.1.0 power_supply_technology
        :param is_present:              uavcan.primitive.scalar.Integer8.1.0 is_present
        :param location:                uavcan.primitive.String.1.0 location
        :param serial_number:           uavcan.primitive.String.1.0 serial_number
        """
        self._voltage:                 uavcan.si.unit.voltage.Scalar_1_0
        self._current:                 uavcan.si.unit.electric_current.Scalar_1_0
        self._charge:                  uavcan.si.unit.electric_charge.Scalar_1_0
        self._capacity:                uavcan.si.unit.electric_charge.Scalar_1_0
        self._design_capacity:         uavcan.si.unit.electric_charge.Scalar_1_0
        self._power_supply_status:     uavcan.primitive.scalar.Integer8_1_0
        self._power_supply_health:     uavcan.primitive.scalar.Integer8_1_0
        self._power_supply_technology: uavcan.primitive.scalar.Integer8_1_0
        self._is_present:              uavcan.primitive.scalar.Integer8_1_0
        self._location:                uavcan.primitive.String_1_0
        self._serial_number:           uavcan.primitive.String_1_0

        if voltage is None:
            self.voltage = uavcan.si.unit.voltage.Scalar_1_0()
        elif isinstance(voltage, uavcan.si.unit.voltage.Scalar_1_0):
            self.voltage = voltage
        else:
            raise ValueError(f'voltage: expected uavcan.si.unit.voltage.Scalar_1_0 '
                             f'got {type(voltage).__name__}')

        if current is None:
            self.current = uavcan.si.unit.electric_current.Scalar_1_0()
        elif isinstance(current, uavcan.si.unit.electric_current.Scalar_1_0):
            self.current = current
        else:
            raise ValueError(f'current: expected uavcan.si.unit.electric_current.Scalar_1_0 '
                             f'got {type(current).__name__}')

        if charge is None:
            self.charge = uavcan.si.unit.electric_charge.Scalar_1_0()
        elif isinstance(charge, uavcan.si.unit.electric_charge.Scalar_1_0):
            self.charge = charge
        else:
            raise ValueError(f'charge: expected uavcan.si.unit.electric_charge.Scalar_1_0 '
                             f'got {type(charge).__name__}')

        if capacity is None:
            self.capacity = uavcan.si.unit.electric_charge.Scalar_1_0()
        elif isinstance(capacity, uavcan.si.unit.electric_charge.Scalar_1_0):
            self.capacity = capacity
        else:
            raise ValueError(f'capacity: expected uavcan.si.unit.electric_charge.Scalar_1_0 '
                             f'got {type(capacity).__name__}')

        if design_capacity is None:
            self.design_capacity = uavcan.si.unit.electric_charge.Scalar_1_0()
        elif isinstance(design_capacity, uavcan.si.unit.electric_charge.Scalar_1_0):
            self.design_capacity = design_capacity
        else:
            raise ValueError(f'design_capacity: expected uavcan.si.unit.electric_charge.Scalar_1_0 '
                             f'got {type(design_capacity).__name__}')

        if power_supply_status is None:
            self.power_supply_status = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(power_supply_status, uavcan.primitive.scalar.Integer8_1_0):
            self.power_supply_status = power_supply_status
        else:
            raise ValueError(f'power_supply_status: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(power_supply_status).__name__}')

        if power_supply_health is None:
            self.power_supply_health = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(power_supply_health, uavcan.primitive.scalar.Integer8_1_0):
            self.power_supply_health = power_supply_health
        else:
            raise ValueError(f'power_supply_health: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(power_supply_health).__name__}')

        if power_supply_technology is None:
            self.power_supply_technology = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(power_supply_technology, uavcan.primitive.scalar.Integer8_1_0):
            self.power_supply_technology = power_supply_technology
        else:
            raise ValueError(f'power_supply_technology: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(power_supply_technology).__name__}')

        if is_present is None:
            self.is_present = uavcan.primitive.scalar.Integer8_1_0()
        elif isinstance(is_present, uavcan.primitive.scalar.Integer8_1_0):
            self.is_present = is_present
        else:
            raise ValueError(f'is_present: expected uavcan.primitive.scalar.Integer8_1_0 '
                             f'got {type(is_present).__name__}')

        if location is None:
            self.location = uavcan.primitive.String_1_0()
        elif isinstance(location, uavcan.primitive.String_1_0):
            self.location = location
        else:
            raise ValueError(f'location: expected uavcan.primitive.String_1_0 '
                             f'got {type(location).__name__}')

        if serial_number is None:
            self.serial_number = uavcan.primitive.String_1_0()
        elif isinstance(serial_number, uavcan.primitive.String_1_0):
            self.serial_number = serial_number
        else:
            raise ValueError(f'serial_number: expected uavcan.primitive.String_1_0 '
                             f'got {type(serial_number).__name__}')

    @property
    def voltage(self) -> uavcan.si.unit.voltage.Scalar_1_0:
        """
        uavcan.si.unit.voltage.Scalar.1.0 voltage
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._voltage

    @voltage.setter
    def voltage(self, x: uavcan.si.unit.voltage.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.voltage.Scalar_1_0):
            self._voltage = x
        else:
            raise ValueError(f'voltage: expected uavcan.si.unit.voltage.Scalar_1_0 got {type(x).__name__}')

    @property
    def current(self) -> uavcan.si.unit.electric_current.Scalar_1_0:
        """
        uavcan.si.unit.electric_current.Scalar.1.0 current
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._current

    @current.setter
    def current(self, x: uavcan.si.unit.electric_current.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.electric_current.Scalar_1_0):
            self._current = x
        else:
            raise ValueError(f'current: expected uavcan.si.unit.electric_current.Scalar_1_0 got {type(x).__name__}')

    @property
    def charge(self) -> uavcan.si.unit.electric_charge.Scalar_1_0:
        """
        uavcan.si.unit.electric_charge.Scalar.1.0 charge
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._charge

    @charge.setter
    def charge(self, x: uavcan.si.unit.electric_charge.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.electric_charge.Scalar_1_0):
            self._charge = x
        else:
            raise ValueError(f'charge: expected uavcan.si.unit.electric_charge.Scalar_1_0 got {type(x).__name__}')

    @property
    def capacity(self) -> uavcan.si.unit.electric_charge.Scalar_1_0:
        """
        uavcan.si.unit.electric_charge.Scalar.1.0 capacity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, x: uavcan.si.unit.electric_charge.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.electric_charge.Scalar_1_0):
            self._capacity = x
        else:
            raise ValueError(f'capacity: expected uavcan.si.unit.electric_charge.Scalar_1_0 got {type(x).__name__}')

    @property
    def design_capacity(self) -> uavcan.si.unit.electric_charge.Scalar_1_0:
        """
        uavcan.si.unit.electric_charge.Scalar.1.0 design_capacity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._design_capacity

    @design_capacity.setter
    def design_capacity(self, x: uavcan.si.unit.electric_charge.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.electric_charge.Scalar_1_0):
            self._design_capacity = x
        else:
            raise ValueError(f'design_capacity: expected uavcan.si.unit.electric_charge.Scalar_1_0 got {type(x).__name__}')

    @property
    def power_supply_status(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 power_supply_status
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._power_supply_status

    @power_supply_status.setter
    def power_supply_status(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._power_supply_status = x
        else:
            raise ValueError(f'power_supply_status: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def power_supply_health(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 power_supply_health
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._power_supply_health

    @power_supply_health.setter
    def power_supply_health(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._power_supply_health = x
        else:
            raise ValueError(f'power_supply_health: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def power_supply_technology(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 power_supply_technology
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._power_supply_technology

    @power_supply_technology.setter
    def power_supply_technology(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._power_supply_technology = x
        else:
            raise ValueError(f'power_supply_technology: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def is_present(self) -> uavcan.primitive.scalar.Integer8_1_0:
        """
        uavcan.primitive.scalar.Integer8.1.0 is_present
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._is_present

    @is_present.setter
    def is_present(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
            self._is_present = x
        else:
            raise ValueError(f'is_present: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

    @property
    def location(self) -> uavcan.primitive.String_1_0:
        """
        uavcan.primitive.String.1.0 location
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._location

    @location.setter
    def location(self, x: uavcan.primitive.String_1_0) -> None:
        if isinstance(x, uavcan.primitive.String_1_0):
            self._location = x
        else:
            raise ValueError(f'location: expected uavcan.primitive.String_1_0 got {type(x).__name__}')

    @property
    def serial_number(self) -> uavcan.primitive.String_1_0:
        """
        uavcan.primitive.String.1.0 serial_number
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, x: uavcan.primitive.String_1_0) -> None:
        if isinstance(x, uavcan.primitive.String_1_0):
            self._serial_number = x
        else:
            raise ValueError(f'serial_number: expected uavcan.primitive.String_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.voltage._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.current._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.charge._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.capacity._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.design_capacity._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.power_supply_status._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.power_supply_health._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.power_supply_technology._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.is_present._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.location._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.serial_number._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 224 <= (_ser_.current_bit_length - _base_offset_) <= 4320, \
            'Bad serialization of voltbro.battery.state.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> state_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "voltage"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.voltage.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "current"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.electric_current.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "charge"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.electric_charge.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "capacity"
        _des_.pad_to_alignment(8)
        _f3_ = uavcan.si.unit.electric_charge.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f4_ holds the value of "design_capacity"
        _des_.pad_to_alignment(8)
        _f4_ = uavcan.si.unit.electric_charge.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f5_ holds the value of "power_supply_status"
        _des_.pad_to_alignment(8)
        _f5_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f6_ holds the value of "power_supply_health"
        _des_.pad_to_alignment(8)
        _f6_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f7_ holds the value of "power_supply_technology"
        _des_.pad_to_alignment(8)
        _f7_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f8_ holds the value of "is_present"
        _des_.pad_to_alignment(8)
        _f8_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f9_ holds the value of "location"
        _des_.pad_to_alignment(8)
        _f9_ = uavcan.primitive.String_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f10_ holds the value of "serial_number"
        _des_.pad_to_alignment(8)
        _f10_ = uavcan.primitive.String_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = state_1_0(
            voltage=_f0_,
            current=_f1_,
            charge=_f2_,
            capacity=_f3_,
            design_capacity=_f4_,
            power_supply_status=_f5_,
            power_supply_health=_f6_,
            power_supply_technology=_f7_,
            is_present=_f8_,
            location=_f9_,
            serial_number=_f10_)
        _des_.pad_to_alignment(8)
        assert 224 <= (_des_.consumed_bit_length - _base_offset_) <= 4320, \
            'Bad deserialization of voltbro.battery.state.1.0'
        assert isinstance(self, state_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'voltage=%s' % self.voltage,
            'current=%s' % self.current,
            'charge=%s' % self.charge,
            'capacity=%s' % self.capacity,
            'design_capacity=%s' % self.design_capacity,
            'power_supply_status=%s' % self.power_supply_status,
            'power_supply_health=%s' % self.power_supply_health,
            'power_supply_technology=%s' % self.power_supply_technology,
            'is_present=%s' % self.is_present,
            'location=%s' % self.location,
            'serial_number=%s' % self.serial_number,
        ])
        return f'voltbro.battery.state.1.0({_o_0_})'

    _EXTENT_BYTES_ = 540

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8n9mbt0{`t=TWlO>72dgT?wh7b+@@_NZJKP_WV=b6WYepAA-J5L)M|P$h%%nto%kPjZ<?7+ZKO)B1jvO!9jQ~v4}dHRk|ioI'
        '6%Q6q7Ek8QASx^nk|kdJz=I!<h>(yt|IV(x7dy_)3ADE4-G9#QKmT{m|NnDVXH@?92kBVt&p%ih$-DVN%5W{mHVgK*&1}I+8M$(?'
        'Qg&_63jG}~Sp~aD!~E+b6)XHGJobM0UYPV%!!DI9CuA{y$0g6H=Dez7wTdW4$t;qIy;sTwFYA<3S<~|@XC&o%CN~{7u2_z1mrLA;'
        '_GW$jQ3wLWz8Ah9`r8araO`Z=v)u4)vbcu3%Tl4QT(GS|e#M8aM&9&H!{d%IEh4h5{)1KXO3o~$Tsu`Q*<Ol!XbxJbOF6S((xSGr'
        'oeeM8?zcm>x31Z>mJ1b!gJfSJ7q(m|lufS{ifu;L_Kbp68uVBQI=PiIUC$_%^W@ece_vliovWo@Bpz}WVG;Xo_*&@SYY=9oyy@hd'
        '4ULhVqB%$lsOI^^mmM?b5r!^dd!ari8~)ML-RV=AQ>VMno;{s8b1IWLb3SwO<hgYB$;|2QO!t|SXV0HH)7_m8`CQd3;UjZELSHuW'
        '<y`2;h-mtInxbK3N21`q7qV`4(4__Dt%_siD6skP1AnJ+*&ep?My2d{hMf;D`nwIcTy=65F$$JZG0A;j<6i|kORo1(x()Yn>PG~Z'
        '@C41x$~<}GDgjNR#j@iX@6yU7*CCg7)Seju@~-KS*!D{KUCS}Dj-4OmsbvjQrj^V>=pU$5vjsb6IM!gbz};KP2(qR|i4gjtYxBtn'
        'OPZ{n4xzs*N{H0SR651O9(p_)duU>p*5FtrkLSS^J7<L-urur|A(kzW*&~fCS&0@2dhO5T_Y1c7O6~a)J=XKZmyB{H^!2rjxFf}E'
        'nbt&}pj9kW4)RF9TCp6{D?815G{<b(4eTv{SD%^B+oiz{A@)tqy;v>KGDq6EWZ{Zgs9NENVG{Jf&C;H&M213$SF^O-qFv$%O#^e7'
        '4>X?C1T@#)YFNV+vsByG7pqw}Tg$CwbU9!|S>9Vs`}0WK{<I2Kj&d(&<f;xwef^Ef9;uIxfX<Gx$Jy~Qc7mmEVlSv>kzi@KYqE2c'
        '^Y5`ME<67Ld-5WCiancT&#@l%JbQt?$X;S!VHem}SucB;ea%m_J07xEcnYysYw5!J*rl4A>`nId<#>E+d6bQqRs()E$WdpEmSofa'
        '5b+94z%I|RHn5Mb2`ufU>p1{#AFf)iTrHG~*%n}b#6G?*V0X1SzLB`9jVan;{g9aPoLMn*wl}gmdsp6a?ZJ|<w$w^&^m=TT?~;@o'
        'ojxy@JZsQ$GS>>rA%FKJn#ju6g<I|)3Rb)xtlEl{XjeA_Kf`{z9`OE_rdv*pd<*^E4eweH$(x8oyg3qaibT9U5__Uk-mO+Dg%N%w'
        'dR4a*(cg4PGRrK`)v~JO{uW8k%CS<pP#zpvU3#lc2ft&v>uj_A9igOmBz|gM<IUp08ZS4FV~&LW{x?mc5+%AVp6ArocZ?kd?TI44'
        'lA^brL;jvOO78XLgui7aLop`!_cZRC%lvh!Ztx$=iV0FY1_Iy8QA({E<+uF3FP2OEm7uih1;r=j_Y<92{OztK7ZN-dnoaG0%`6RC'
        'uUQq#v)8)q-l<(e<o_y(RZFTEvoTi7sw4=U6AM7Be@nG*ij5e6T&F3^G>||JK#iV7KGs@zpnw`cyso#Ug9jRU0b7^#i9*lYR+WP-'
        'ur+|~5iic?+Oeh_Y=i9q>};`1RHE&=rVi|YodG23a|Ez^U1``wL4kWZW+D#J_gt4g?1p;+xHpoOiNBre?!9hZ*aP<luy0i#h)cZv'
        'H)IR;!oC2y8c35b_ua5Q?1!!Z?qAa<k|6$po3ab{!TkX|(1I6n$=-uEZ4VB>0|7jAO@B#>WDefa9Pl7K6o9^rE%*A+En9?xbYa88'
        'ksbY7{`1)%xh?a-A$T}|!;Lwc;=oaQ^tR0bkHFyoj;tFQ($GnoWRKp~x#3Yb5<s%C&U(y_-S#=)C?o@T?7G)U8YKVthWG);;IROX'
        'uf+B+*-SRa_r!+H3y;I`08%%E18I@Y6C3IioPbmS>6JW4MwxJO!)JvjARWM|8%BgQN$>O>@efYIsQ|h=Gv+wiPB*gV%pLOuPD6J9'
        'XKxBK(k9(=chpxn17`!sv}RYD=hyi=?gyNMOaM>bG<IZx^q;ybe#3cqGJvPo&ckk+Bg1p?nY-p6JOxh&@a!$&OIFCnb9Z$O@C-Z~'
        'Ku<@`QuM2=P$OeZ#F&gRl?n`qV_d|zj8_$mtB}BihzS`JDs*9&h+Q&vsd!Zb9d!|P8Fdwsm=rN7V^W1QrbSH4m{uW!84)uwW>o0G'
        '9ua$F>`|c?dqwP(u~&sY>=Ut1#y%DLv0ub~8T(ZjzyT2lWE@a|Arq0w$W*9cMZ}7X6%~eYSj1r&hgBHGQ4vRF993Zq$3z^HaZH5('
        '0}%rm0~N+`T*Pr1$5oiX2@xk`oKRsBCq<l;aZ-gToDy+L#wiu1aazP_8K+g4!5I-}WSmi97H37Am2p;uIh+%5PR2PE=5b!cc^T(b'
        'Sil7l7i3&eVG$QaT$FK9g(X}PaY@D{6|Uk{5w8-Sgsy-w31bSzG>i)vmoQEsYnTu)Az?zngoa%Lc1hT!V3&rvfVzabg1UxD0h1CY'
        '6-;WF7BDSgTEVo2838jAW)#e5*dt(%ggpxOXxJ-YuY|n{_G;KCV4sA23ifH(FJQlf{R;MLI3VDFgaZl=XvhR)5;6suh7|!T5>^zf'
        'XgDn3u!O@34r@3n;HZS73XW<xCg7NaV+xLG7zh|h7$_KMI4<D0gyRa1Yd9g`goG0cPG~qO;G~3;3QlS`CE%2VQwmOLI4$6`gwqO6'
        'Yd9m|jD#}^&S*F*;H-qR3eIXcC*Yifa|+IBI4|J5gjXe;S8!g#1pyZ%Tu^X9!$koXC0tZ+QNtwxmn2+La7n|fLQu_GE-#`JR75BK'
        'pNi->FP=7w=sQqECn6j+i|7p~qUjYpLie^7(fWE9^9B^rdTSiMutl`K^25iMrikWiK1`OAt?~U*7ttJ(WFr$ci|Do@x;0}qi|89I'
        'qN7tLNxZ~n5q%3qbaX3i7SVU2h+a7nn~Uh?5}N8}jK>=_v{<j9RVqAqCC!WIS}`r(%`%$GXR4!lF)goNM)UHyUP*73(O=XuI;x?m'
        'n7-~Zy57vt*@Q6^2(cLZ`??J<zw>uR?F6f|T=?IAUVr2D3z-vEDOb*0dEKo^>gCJ2XAOI)t(WXl&eA<*H8{4bJ664?f#gkBH}(8T'
        '$t>DAz1Dodb+aR$<sR2<kBgVeo?faJ3MV|vDcU98RF~3UvEQ-uK9jeF)GepN^}0X)wcPHp@}oj?zel`K&ed86I(setM(iC?r-V_e'
        '7PGt+wI*Y6B$KSj_A#H8*e}=**)Q3r?APp9><{cS_9ym7_Gk7v`wN>N`Z0(5uR{~`HS`nusICdTzdbinVJ59OY8%w*Ev+=FH?@ZT'
        '&RSdRO?APn(Ec5X{fGBMY)bwwNq%FECNcJ%=x4DWqV}v%8^UemPa@#~q7HNlw~_0@qeLC;6mBEeg(rwQ(J9<U{(U4oNz}<s;Wlzz'
        'c#5b~ox*M8y6`knr#pq)$aUcvqRw;*w~~j(X@^Ggb97kD#XA++=uH|6#92smYP8X#V~1^H+gXBlXC>(nDbWG)DIFf4(ZTUKo2T=F'
        '9~B#N$_)LK%Y4E=e#Sq3P9IIDh_4yEt-0id<g>re$k#jb9p2xTr?2)lE#9E{&ucVjHK%+>OXRZHkV0-m4?}Sp;sfHf`l}*18^7YZ'
        'HC&@0=)C)CcPE!Cr~V6c#d3O<FaQ7'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
