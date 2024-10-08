# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/mors_ws/src/mors_hardware/power_bridge/cyphal-types/voltbro/config/six_step/pid_config.1.0.dsdl
#
# Generated at:  2024-04-08 11:06:00.220273 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.config.six_step.pid_config
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


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class pid_config_1_0:
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
                 p_gain:             None | uavcan.primitive.scalar.Real64_1_0 = None,
                 i_gain:             None | uavcan.primitive.scalar.Real64_1_0 = None,
                 d_gain:             None | uavcan.primitive.scalar.Real64_1_0 = None,
                 integral_error_lim: None | uavcan.primitive.scalar.Real64_1_0 = None,
                 tolerance:          None | uavcan.primitive.scalar.Real64_1_0 = None) -> None:
        """
        voltbro.config.six_step.pid_config.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param p_gain:             uavcan.primitive.scalar.Real64.1.0 p_gain
        :param i_gain:             uavcan.primitive.scalar.Real64.1.0 i_gain
        :param d_gain:             uavcan.primitive.scalar.Real64.1.0 d_gain
        :param integral_error_lim: uavcan.primitive.scalar.Real64.1.0 integral_error_lim
        :param tolerance:          uavcan.primitive.scalar.Real64.1.0 tolerance
        """
        self._p_gain:             uavcan.primitive.scalar.Real64_1_0
        self._i_gain:             uavcan.primitive.scalar.Real64_1_0
        self._d_gain:             uavcan.primitive.scalar.Real64_1_0
        self._integral_error_lim: uavcan.primitive.scalar.Real64_1_0
        self._tolerance:          uavcan.primitive.scalar.Real64_1_0

        if p_gain is None:
            self.p_gain = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(p_gain, uavcan.primitive.scalar.Real64_1_0):
            self.p_gain = p_gain
        else:
            raise ValueError(f'p_gain: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(p_gain).__name__}')

        if i_gain is None:
            self.i_gain = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(i_gain, uavcan.primitive.scalar.Real64_1_0):
            self.i_gain = i_gain
        else:
            raise ValueError(f'i_gain: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(i_gain).__name__}')

        if d_gain is None:
            self.d_gain = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(d_gain, uavcan.primitive.scalar.Real64_1_0):
            self.d_gain = d_gain
        else:
            raise ValueError(f'd_gain: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(d_gain).__name__}')

        if integral_error_lim is None:
            self.integral_error_lim = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(integral_error_lim, uavcan.primitive.scalar.Real64_1_0):
            self.integral_error_lim = integral_error_lim
        else:
            raise ValueError(f'integral_error_lim: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(integral_error_lim).__name__}')

        if tolerance is None:
            self.tolerance = uavcan.primitive.scalar.Real64_1_0()
        elif isinstance(tolerance, uavcan.primitive.scalar.Real64_1_0):
            self.tolerance = tolerance
        else:
            raise ValueError(f'tolerance: expected uavcan.primitive.scalar.Real64_1_0 '
                             f'got {type(tolerance).__name__}')

    @property
    def p_gain(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 p_gain
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._p_gain

    @p_gain.setter
    def p_gain(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._p_gain = x
        else:
            raise ValueError(f'p_gain: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    @property
    def i_gain(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 i_gain
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._i_gain

    @i_gain.setter
    def i_gain(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._i_gain = x
        else:
            raise ValueError(f'i_gain: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    @property
    def d_gain(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 d_gain
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._d_gain

    @d_gain.setter
    def d_gain(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._d_gain = x
        else:
            raise ValueError(f'd_gain: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    @property
    def integral_error_lim(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 integral_error_lim
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._integral_error_lim

    @integral_error_lim.setter
    def integral_error_lim(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._integral_error_lim = x
        else:
            raise ValueError(f'integral_error_lim: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    @property
    def tolerance(self) -> uavcan.primitive.scalar.Real64_1_0:
        """
        uavcan.primitive.scalar.Real64.1.0 tolerance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, x: uavcan.primitive.scalar.Real64_1_0) -> None:
        if isinstance(x, uavcan.primitive.scalar.Real64_1_0):
            self._tolerance = x
        else:
            raise ValueError(f'tolerance: expected uavcan.primitive.scalar.Real64_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.p_gain._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.i_gain._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.d_gain._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.integral_error_lim._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.tolerance._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 320 <= (_ser_.current_bit_length - _base_offset_) <= 320, \
            'Bad serialization of voltbro.config.six_step.pid_config.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> pid_config_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "p_gain"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "i_gain"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "d_gain"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "integral_error_lim"
        _des_.pad_to_alignment(8)
        _f3_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f4_ holds the value of "tolerance"
        _des_.pad_to_alignment(8)
        _f4_ = uavcan.primitive.scalar.Real64_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = pid_config_1_0(
            p_gain=_f0_,
            i_gain=_f1_,
            d_gain=_f2_,
            integral_error_lim=_f3_,
            tolerance=_f4_)
        _des_.pad_to_alignment(8)
        assert 320 <= (_des_.consumed_bit_length - _base_offset_) <= 320, \
            'Bad deserialization of voltbro.config.six_step.pid_config.1.0'
        assert isinstance(self, pid_config_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'p_gain=%s' % self.p_gain,
            'i_gain=%s' % self.i_gain,
            'd_gain=%s' % self.d_gain,
            'integral_error_lim=%s' % self.integral_error_lim,
            'tolerance=%s' % self.tolerance,
        ])
        return f'voltbro.config.six_step.pid_config.1.0({_o_0_})'

    _EXTENT_BYTES_ = 40

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8n9mbt0{^{M>u=md5WlExlBO?8XaOP7D<4W)+QV<Jiv*!B2^~$N6bdbrWqsb>Eck4*UMD%A(0%|l!h%X&{-6G7%$_gFB~6ON'
        '2Tt;NcV0U)`<od*I{5eeTx;~J&lJO?OwtZ5xfCoFKe9OG9oowWMP3TUb$#p_PsIS2$!EiY>u37>WBpJs)YDXC8J8Mb^|9MZRy|co'
        'zEk87&Da1<ytA68DwcVtmuC+|zf+2JS}I<23X#x;rt4X{%4I3?%vhYcGhRQ_-KlQtcl}t`M<`QDinvm|)c4W+KE7{B>H5$O!P8{h'
        'p*fl`#i%k~!c0Six%%yjt@c>fDWnNhtnyCTV=0rJ70%MY({L1yZ@K{|?`t?UR()eXAGR#%`tXf3XKH6+j?h>rn)0l#KzA3>uO2HE'
        '9pnl6b+$geys2)~I#-c*)37iZt>5&Du3y9Su`FRSnKbkS?F?8y6RJwg!4D+sDNJIC$-OaNqm3{9saDGlqcDhE+x1A`xV9f!#P)nA'
        '^c**I?a=aEKL{gYg%-Yj$0wc_MS&lY$PT?QAePZ_0xKkz<q+Q`VPN?r@_iDxP8b9vBz9=~p5+;;>)W1794|ogp6l4I6A%*N)+Q)S'
        'JUjv)%k|yRw}XfT7M^BXei-<^?GVQb1IP2d$g(2KC6Vi(vS)>O81XIQp^)oFXxp6TI&Oecj^jigu>+r2#P=f?Pjy_37DL3)i4!=M'
        'XM0|V!K1S-dK=oritNaVB0_A(x6pUX32frojz`dLK(tAI6(eE}t+KSj93P}f-qW>peI3)A4%?C!l9xPF1_o`BDc(mQUv7VO$+>XB'
        'cQ3Zz8@=zN6;{tr0Gh_brdS?o@Zd~|5J`-!9>c=Z8})JeK&<nG7P(YZBzmbnNz1&FJ&uf&(}E!Y>KXG&MU0ofjODw&Y^cu=a8vK2'
        'uaKK!JXj%AQFM^YlCB{(4wMo@I5ye?LTZgk6gyhvYh2P;ilmR*S-!5g%vh@Hw~8uGMUP6}uTtaQc2S|V>86&@gNYiLZt6+bCz^`t'
        '*d425>P9OA=XpH0#1JGV&J@zB=yAOPe%&$|j#D&yZnMs|@s5&e_a6PeBGjj&{cYTiE3Q63^Fr6{{fv~uL7Zbu=*mq#$gzq|t=uZO'
        'WGa`FJ+B7>8wz|;pIBx|BC`GqLh!ZWE>$T8JlxGi3k`Dq(hJ?ir)7+7uV@VE?rarfxC4=ymVgVkZWc49EnuRJ_8jHw1<OXAajA;S'
        'cm&4jg7z6|fe*Kku+^O4O~Vu~V<s<QzB+=hWGUrR=91zR*jw<h%2Nz8!%J)U974k#z-cHTgA#s#RZuX5wF;sQxV!`(z=sR)5iG*T'
        'a0RZyHMm|M?F|cH>7_A_X2vrEQ?@lBHs=Oj)Ar=pi6vOtFh0OC+#dM|ci`^Uy?nE^x;t@Kr>^FiDYI<PORo<%caGRJL+4+t{m~ry'
        '=l>~r5Bdf=0Nq6p_<V=LDWU`J@zPKqA@$KVbyIj3c`W=Ksn1^&-bHSNZ?>jDn7`fPFEYjoi-x|qhr(_~gKRj0llK)faTgFu8Nx`x'
        '+J6BT`~*M4L-+-LoxliImT794(s*)x8vAYYog*o5mf)-TOgLN5e~uN`&v^1l)6aLzayZv*!@F?4J7tCgTzrC#?+L!iYmA#UH(j8O'
        'U0??uUteKapRe$OE3sc2`o8H7Mq$#{?9)-=pxfF?XLr^xT2ISSUYkp9Blp`qxJJ42535>ziyjI900'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
