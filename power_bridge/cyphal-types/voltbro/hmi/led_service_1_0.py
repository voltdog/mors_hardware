# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/user/mors_ws/src/mors_hardware/power_bridge/cyphal-types/voltbro/hmi/led_service.1.0.dsdl
#
# Generated at:  2024-04-08 11:06:00.253826 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     voltbro.hmi.led_service
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
import uavcan.si.unit.duration
import uavcan.si.unit.frequency


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class led_service_1_0:
    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Request:
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
                     r:         None | uavcan.primitive.scalar.Integer8_1_0 = None,
                     g:         None | uavcan.primitive.scalar.Integer8_1_0 = None,
                     b:         None | uavcan.primitive.scalar.Integer8_1_0 = None,
                     duration:  None | uavcan.si.unit.duration.Scalar_1_0 = None,
                     frequency: None | uavcan.si.unit.frequency.Scalar_1_0 = None,
                     interface: None | uavcan.primitive.scalar.Integer8_1_0 = None) -> None:
            """
            voltbro.hmi.led_service.Request.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param r:         uavcan.primitive.scalar.Integer8.1.0 r
            :param g:         uavcan.primitive.scalar.Integer8.1.0 g
            :param b:         uavcan.primitive.scalar.Integer8.1.0 b
            :param duration:  uavcan.si.unit.duration.Scalar.1.0 duration
            :param frequency: uavcan.si.unit.frequency.Scalar.1.0 frequency
            :param interface: uavcan.primitive.scalar.Integer8.1.0 interface
            """
            self._r:         uavcan.primitive.scalar.Integer8_1_0
            self._g:         uavcan.primitive.scalar.Integer8_1_0
            self._b:         uavcan.primitive.scalar.Integer8_1_0
            self._duration:  uavcan.si.unit.duration.Scalar_1_0
            self._frequency: uavcan.si.unit.frequency.Scalar_1_0
            self._interface: uavcan.primitive.scalar.Integer8_1_0

            if r is None:
                self.r = uavcan.primitive.scalar.Integer8_1_0()
            elif isinstance(r, uavcan.primitive.scalar.Integer8_1_0):
                self.r = r
            else:
                raise ValueError(f'r: expected uavcan.primitive.scalar.Integer8_1_0 '
                                 f'got {type(r).__name__}')

            if g is None:
                self.g = uavcan.primitive.scalar.Integer8_1_0()
            elif isinstance(g, uavcan.primitive.scalar.Integer8_1_0):
                self.g = g
            else:
                raise ValueError(f'g: expected uavcan.primitive.scalar.Integer8_1_0 '
                                 f'got {type(g).__name__}')

            if b is None:
                self.b = uavcan.primitive.scalar.Integer8_1_0()
            elif isinstance(b, uavcan.primitive.scalar.Integer8_1_0):
                self.b = b
            else:
                raise ValueError(f'b: expected uavcan.primitive.scalar.Integer8_1_0 '
                                 f'got {type(b).__name__}')

            if duration is None:
                self.duration = uavcan.si.unit.duration.Scalar_1_0()
            elif isinstance(duration, uavcan.si.unit.duration.Scalar_1_0):
                self.duration = duration
            else:
                raise ValueError(f'duration: expected uavcan.si.unit.duration.Scalar_1_0 '
                                 f'got {type(duration).__name__}')

            if frequency is None:
                self.frequency = uavcan.si.unit.frequency.Scalar_1_0()
            elif isinstance(frequency, uavcan.si.unit.frequency.Scalar_1_0):
                self.frequency = frequency
            else:
                raise ValueError(f'frequency: expected uavcan.si.unit.frequency.Scalar_1_0 '
                                 f'got {type(frequency).__name__}')

            if interface is None:
                self.interface = uavcan.primitive.scalar.Integer8_1_0()
            elif isinstance(interface, uavcan.primitive.scalar.Integer8_1_0):
                self.interface = interface
            else:
                raise ValueError(f'interface: expected uavcan.primitive.scalar.Integer8_1_0 '
                                 f'got {type(interface).__name__}')

        @property
        def r(self) -> uavcan.primitive.scalar.Integer8_1_0:
            """
            uavcan.primitive.scalar.Integer8.1.0 r
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._r

        @r.setter
        def r(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
            if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
                self._r = x
            else:
                raise ValueError(f'r: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

        @property
        def g(self) -> uavcan.primitive.scalar.Integer8_1_0:
            """
            uavcan.primitive.scalar.Integer8.1.0 g
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._g

        @g.setter
        def g(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
            if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
                self._g = x
            else:
                raise ValueError(f'g: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

        @property
        def b(self) -> uavcan.primitive.scalar.Integer8_1_0:
            """
            uavcan.primitive.scalar.Integer8.1.0 b
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._b

        @b.setter
        def b(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
            if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
                self._b = x
            else:
                raise ValueError(f'b: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

        @property
        def duration(self) -> uavcan.si.unit.duration.Scalar_1_0:
            """
            uavcan.si.unit.duration.Scalar.1.0 duration
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._duration

        @duration.setter
        def duration(self, x: uavcan.si.unit.duration.Scalar_1_0) -> None:
            if isinstance(x, uavcan.si.unit.duration.Scalar_1_0):
                self._duration = x
            else:
                raise ValueError(f'duration: expected uavcan.si.unit.duration.Scalar_1_0 got {type(x).__name__}')

        @property
        def frequency(self) -> uavcan.si.unit.frequency.Scalar_1_0:
            """
            uavcan.si.unit.frequency.Scalar.1.0 frequency
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._frequency

        @frequency.setter
        def frequency(self, x: uavcan.si.unit.frequency.Scalar_1_0) -> None:
            if isinstance(x, uavcan.si.unit.frequency.Scalar_1_0):
                self._frequency = x
            else:
                raise ValueError(f'frequency: expected uavcan.si.unit.frequency.Scalar_1_0 got {type(x).__name__}')

        @property
        def interface(self) -> uavcan.primitive.scalar.Integer8_1_0:
            """
            uavcan.primitive.scalar.Integer8.1.0 interface
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._interface

        @interface.setter
        def interface(self, x: uavcan.primitive.scalar.Integer8_1_0) -> None:
            if isinstance(x, uavcan.primitive.scalar.Integer8_1_0):
                self._interface = x
            else:
                raise ValueError(f'interface: expected uavcan.primitive.scalar.Integer8_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.r._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.g._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.b._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.duration._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.frequency._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            self.interface._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
                'Bad serialization of voltbro.hmi.led_service.Request.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> led_service_1_0.Request:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f0_ holds the value of "r"
            _des_.pad_to_alignment(8)
            _f0_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f1_ holds the value of "g"
            _des_.pad_to_alignment(8)
            _f1_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f2_ holds the value of "b"
            _des_.pad_to_alignment(8)
            _f2_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f3_ holds the value of "duration"
            _des_.pad_to_alignment(8)
            _f3_ = uavcan.si.unit.duration.Scalar_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f4_ holds the value of "frequency"
            _des_.pad_to_alignment(8)
            _f4_ = uavcan.si.unit.frequency.Scalar_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            # Temporary _f5_ holds the value of "interface"
            _des_.pad_to_alignment(8)
            _f5_ = uavcan.primitive.scalar.Integer8_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = led_service_1_0.Request(
                r=_f0_,
                g=_f1_,
                b=_f2_,
                duration=_f3_,
                frequency=_f4_,
                interface=_f5_)
            _des_.pad_to_alignment(8)
            assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
                'Bad deserialization of voltbro.hmi.led_service.Request.1.0'
            assert isinstance(self, led_service_1_0.Request)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'r=%s' % self.r,
                'g=%s' % self.g,
                'b=%s' % self.b,
                'duration=%s' % self.duration,
                'frequency=%s' % self.frequency,
                'interface=%s' % self.interface,
            ])
            return f'voltbro.hmi.led_service.Request.1.0({_o_0_})'

        _EXTENT_BYTES_ = 12

        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8n9mbt0{_ib+io015M3v}>?RJe<$xkU*zk}zpiF#OJ7eG}mMjHdVq!oRV6}T@+FLEn&J5i>>)nU|eju`?7C~|&-gx5?#4jN6'
            '6Z}o8cV_Qd5+NaBY31(fn(9;MR8@aB`qST~Li110CXGM_p+h7SoQC`n^+M(lKdvUR<cb-6WlxFJSE*p1G!kac&8-vj*v#uO645H2'
            '&(`8lc_Mb8%AJq}Hd2lI%z4PZN|{tf7fFo?$>YdCK~H>^ug}fq$Y$Y*IWhV&p-KtvrHV;&fU$?5YI_+yw!v8#bkJNP0acVJ3lT14'
            'Mi|p`DXsZ5auUI-T=5!nq)$UCocobt6((E*6Hsaafyn~{Q~Ad;!%(zi89lwnD-jFwV7>fYCLUKLWKl(d*(@SLpGrllaexTl)UWNf'
            '!r0H8bv)a)M@UQId-KrfYeXs<1ylsxflgBo(;BPMFva^vNf7%+7fk9=J=4V^@fw*tj}6Sj>k`ofED_A7iUsCOze0|99kohgp$HGm'
            'j-DnmPKD3#AY>$=c$c2A|3dB=UE0NJsP9_qIp#KU2k(a1%0HSSJLp=Cg(Sz)=!;Syq$|xmAo^n}&}}k_kC`Bz;6VkqMOIf#L^L$|'
            'jU@F#?i0Z(X=vefl*DM`nSh9(i}vwMMC89EqqFENI94p9EO#?_v&19>i&U!~%^BQ+cabtL#JD$F+IF}_N7cVa;P<%NYVP-No2#oY'
            'k~lGXZdef6sCqFbg-EtpHO9(OSn>}NCa8)<r$)w!4;;%FKGIirX%O(JGT;Oc?CDM#V#baBQ;d+6!c#N9S^QCY*lbA_2x~6&Fx@JT'
            'Z294W*6m`#mLM{1zrI9RJ)u#vA9qqudd=z@5yn!5>vk`|HEXX7v3rB|P7A)3x1i)s8gb<Wsc5p{>}4VjZ$Rvl(nc6l)zet;_U0VC'
            '12^F2DdMlv3I<KFadhcOP~S#Id5atQ8b8xFm&*%F?$UC3b#>WYS#sT#HFt6G?m~IdT`s%jmBrPyrIm7d!PvfQGB7TgA4fr+7KQh)'
            'jlPCh!tFC~cHj;y&BHR3VFgy<F1WA;@52Z1p}ruw?FdAK5L$^EeKkw9w@Be$vmjv|HkygSeb{O%{&9QtX?D181)f8J;d84ie1Rl<'
            'iN6CpBOU2Fm;Qqyvweyj2|KAHzwr{1hyf8Gh5Emscnp|Ok9rvX1%7@J!|)A!YlY4M8#wvTsO-Mwc~xKHID5nq#mSPLGn>Rb9KtmC'
            'K;Z}i_yH>L8$5+S;P-TBW_r?ZBtXO4`N*5dA5@$&_@v@P(EX_PmC)(S<h|83NM2o!Bl`$M&z(rRlno@DoAw=kL9{=!OaJ<RdTzJn'
            'Euy@|w!E;-q_s|=b*f`+Iro`!=j&*_KIq(Mev&!6Xmtmj`^>*)&iiQHA9U_B=P(Y@dN}CZYqs_4JOgJsV+7<0000'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    # noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
    class Response:
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
                     accepted: None | uavcan.primitive.scalar.Bit_1_0 = None) -> None:
            """
            voltbro.hmi.led_service.Response.1.0
            Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
            :param accepted: uavcan.primitive.scalar.Bit.1.0 accepted
            """
            self._accepted: uavcan.primitive.scalar.Bit_1_0

            if accepted is None:
                self.accepted = uavcan.primitive.scalar.Bit_1_0()
            elif isinstance(accepted, uavcan.primitive.scalar.Bit_1_0):
                self.accepted = accepted
            else:
                raise ValueError(f'accepted: expected uavcan.primitive.scalar.Bit_1_0 '
                                 f'got {type(accepted).__name__}')

        @property
        def accepted(self) -> uavcan.primitive.scalar.Bit_1_0:
            """
            uavcan.primitive.scalar.Bit.1.0 accepted
            The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
            """
            return self._accepted

        @accepted.setter
        def accepted(self, x: uavcan.primitive.scalar.Bit_1_0) -> None:
            if isinstance(x, uavcan.primitive.scalar.Bit_1_0):
                self._accepted = x
            else:
                raise ValueError(f'accepted: expected uavcan.primitive.scalar.Bit_1_0 got {type(x).__name__}')

        # noinspection PyProtectedMember
        def _serialize_(self, _ser_: _Issue110_) -> None:
            assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
            _base_offset_ = _ser_.current_bit_length
            _ser_.pad_to_alignment(8)
            self.accepted._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
            _ser_.pad_to_alignment(8)
            assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
                'Bad serialization of voltbro.hmi.led_service.Response.1.0'

        # noinspection PyProtectedMember
        @staticmethod
        def _deserialize_(_des_: _Issue110_) -> led_service_1_0.Response:
            assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
            _base_offset_ = _des_.consumed_bit_length
            # Temporary _f6_ holds the value of "accepted"
            _des_.pad_to_alignment(8)
            _f6_ = uavcan.primitive.scalar.Bit_1_0._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            self = led_service_1_0.Response(
                accepted=_f6_)
            _des_.pad_to_alignment(8)
            assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
                'Bad deserialization of voltbro.hmi.led_service.Response.1.0'
            assert isinstance(self, led_service_1_0.Response)
            return self

        def __repr__(self) -> str:
            _o_0_ = ', '.join([
                'accepted=%s' % self.accepted,
            ])
            return f'voltbro.hmi.led_service.Response.1.0({_o_0_})'

        _EXTENT_BYTES_ = 1

        _MODEL_: _pydsdl_.StructureType = _restore_constant_(
            'ABzY8n9mbt0{?YXTWb_C6yDlycY9My#Rn_slWdhvy<c8iDCqXGw&H_YVrC}p31lWA$!vFpf_+e22q-lE6@Q;6dvB!+!=B7J`SP9f'
            'eUoo9fBw#tdOvqZbyAaxh#00h75poW1&c@`GbIhT%)6yStBb@In!W2N=Fj}vsXy^GS0*{lFn_ltg^jh0Amfo>X+Uc6ghdC;D4829'
            'sgf4chRfVT$yMGD;xk{Ls+WHFQ|}fCwN~@Eu*~=)e;KP$k$2^7&O|z9Gfz@#DY1bfT<O1rvRf@^E1`L$G|#x@Ef$%C3aX<`Zaq|B'
            'Zb$(Zk33u->|42vzz7B@Z%Qc`&Cd^IfyCSr!SbdBY!7KA)L4?q6lvXdHycBMur1oc+-^wWC`#Y`fp<5Eu{2MqPA7r7MU1_aTT~Qy'
            '@(f93;$6uXF?A~wlOu7bugQsr8r(9-CS^*qgj$yRuDeRU@HPshq_%{oe$OovBMY4{ObA94#j{)`{0Sa=H`hQ5v>V~=8TK}{foFpZ'
            'n$HwC7c9-BHssiNH*GXhTI#I<*&kDlWs6E4GfiU6(`K*%Yg?vsD!f}&MJ#wiG;0<j&>PE#XtRCQkio>jXZy+_Dry%!iXKKmA#cOj'
            'R`5`R{58w%(0{%QYj7W@6$^yCHxzU{RxGp^*M0Pz-ue)i17Y1XkqWJT8Hnj*vBZ9m$u7$z+Qp*7_Z8FBN<Fs6EJ=W)ZQ+f()}U$1'
            '^X7j=uphE}g}`Pz7qf`acfl`Tt55wlF@9UB59I6BBF1(zo?{pS+73Y_xDSUMcFz;mRy6N@etSi1;-0apG)b5W9tjgeSHS~x&}UdS'
            'u-=7e4>sU&4W7VLcm~hm1-yh;ZZYX7pkjTXSY>bt;H2;xKp#(D1n0DZ&7a{E*n;g|NAMbUMvcE6MZ54J^aCI3RrrL@5mu4`<>(*v'
            '925V+1ONa'
        )
        assert isinstance(_MODEL_, _pydsdl_.StructureType)

    def __repr__(self) -> str:
        return 'voltbro.hmi.led_service.1.0()'


    _MODEL_: _pydsdl_.ServiceType = _restore_constant_(
        'ABzY8n9mbt0{_ic>rW&_5Z{%@F0VVtc_-!)!7q0hWmuMlTYL)%YS!a8xLhtKm!W5-*=n4f8GCvbmV`v2ULba&3GD|HzxmCNnv0J='
        'z{I~wt9ND}?A`*=m`K8GcXf63uj*G--JkV;``u`&{wJq`niD#%VTP15;<5u`xzsRizY_Q%6I98OEy}CRrVnZXRj2BeBXy`|<e16n'
        'rx6W>DYP6?a%@ZR$QBXr&>S#5Qb9XYRo@jB_YJ5p!=;WsQQI{(V?#=2%_`*~^F3`Y^Dr5os#3a?dZLaHib;gv%!&jJ)nl~X1AS9V'
        '$$>RSU8jX+*mQ^>3Fu5Lgkd=yk*ZBRBjBvU1glabw24c&@u4SZnew87QMl3o0uzrFTu(Mn_CnFLrR2mGD|^&QjGc|oh-ooly3{KR'
        'P^By)v<Zf_;yZ}&WqD(xVMcE=R&njFUc#`XzEqn^K5vGCcn;xCyP@OALbnF0#EtO$e$(-7B~vQ0h`iPoMboOq^c*Ufg{ctHI5gnY'
        'CW1QZL|!p>*gkR<_*|IGQR{NT4E>1P6c=1-1_aNN8U5ojOUa=P%$ofTEj>lw(sOt=_?rIy2&03l6`zOZUZ`YW$Pv<5eGZ6zk8o5Q'
        '4g5XIO^Y+9jMFUL7nFO%Rq|#KSuV3N@5+&@;kB4VYlAU?h@dU(gE5I1{|1f5ypc0BSxV^GUBi<@bb?b)H1biMfB|zDGRsA~w;J5G'
        'VvCBRbB@4QnE0qZ-@<9auIw}YK*{M|M#5Uf^3f?oa+g+o%p8F!e=ne%2%oodWYDyMVH(3dd3A$04)e-gO7K9hu179<T<cs#3vnuZ'
        't!7HuZ$b-;Er<<a&P5iwTVb9~KOB&KJ;>-3#7OJi!zSGih*z)2^~egXdUmC`(xJj}vlie*Eid<wTix<j3BHt+V91QfW5RGEUXO;c'
        '6_ePz0I^Dj)?A;6Gld1WO4D!~UWM0=5r2i0(P)H)BZqc4v9)ESH@lXMahtroP{`$r`GvyL(n4`DUo0*z7w6~i<O=h}g+j5gIKQ-<'
        'Un~@IO4nUI0)rv7ea}hUB9Ox}Isy?w{sb1*p#XPgpa{$GI=lgI!dvh*yaVsTd-A!E>54!^2%+Jql2>C_&n79nUr$K*07`YoU>)u^'
        '8GqOueH<@7)&x%@!C-1$VH<-$@ZZ8Ur$t@s&~q4>>R@E2-ts-Wb_q)Mx=4TnIQ$189stV4!I=pE0N-B}VfY-r&_pMI6+HRRLfL-G'
        'v$B4OVejEP1UpN-PPG#=K;Z@e?7%0$;1pc=2^2hqpQE0h$x*u&0C8uNmX}E`RO~W%rQ$`<eyMh((D7ybzTehJuCMx@z688yb|g6z'
        'Hze$v`X0W(+8^<ufBru;H=Fckk=|^RUf86emX4!zyd`ZYcZd_^Nt8}@D|d*$ij|8fEp{t+h<}WgAEES7w{nL#fw7I!?QZ3>Vx7Nu'
        '!E+i0*b8a*o2d7LE#9H)f4rmaTib8;dQ#y<d44k=S@C_B60ftJr{hj?(*Cq*>kGRR=~QZW1V0ychZR_@U)cY;)27?o!`b|4bXsED'
        'G|;c9cBs=DYTx-#e}P}&H~9VX1-v_n2G2+HLJv-xRL-<9k;M&}<eA^y+y2td@n$NtwYJ?k?cJ>Y<n<?qpXic)p2UWXzX7ht4nd?0'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.ServiceType)