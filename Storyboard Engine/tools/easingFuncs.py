# Original realization in Damnae's Storybrew
# https://github.com/Damnae/storybrew/blob/master/common/Animations/EasingFunctions.cs
import math

Reverse = lambda func, value: 1 - func(1 - value)
ToInOut = lambda func, value: 0.5 * (func(2 * value) if value < 0.5 else 2 - func(2 - 2 * value))
Linear = lambda x: x
QuadIn = lambda x: x*x
QuadOut = lambda x: Reverse(QuadIn, x)
QuadInOut = lambda x: ToInOut(QuadIn, x)
CubicIn = lambda x: x**3
CubicOut = lambda x: Reverse(CubicIn, x)
CubicInOut = lambda x: ToInOut(CubicIn, x)
QuartIn = lambda x: x**4
QuartOut = lambda x: Reverse(QuartIn, x)
QuartInOut = lambda x: ToInOut(QuartIn, x)
QuintIn = lambda x: x**5
QuintOut = lambda x: Reverse(QuintIn, x)
QuintInOut = lambda x: ToInOut(QuintIn, x)

SineIn = lambda x: 1 - math.cos(x * math.pi / 2)
SineOut = lambda x: Reverse(SineIn, x)
SineInOut = lambda x: ToInOut(SineIn, x)

ExpoIn = lambda x: math.pow(2, 10 * (x - 1))
ExpoOut = lambda x: Reverse(ExpoIn, x)
ExpoInOut = lambda x: ToInOut(ExpoIn, x)

CircIn = lambda x: 1 - math.sqrt(1 - x * x)
CircOut = lambda x: Reverse(CircIn, x)
CircInOut = lambda x: ToInOut(CircIn, x)

BackIn = lambda x: x * x * ((1.70158 + 1) * x - 1.70158)
BackOut = lambda x: Reverse(BackIn, x)
BackInOut = lambda x: ToInOut(lambda y: y * y * ((1.70158 * 1.525 + 1) * y - 1.70158 * 1.525), x)

BounceOut = lambda x: 7.5625 * x**2 if x < 1 / 2.75 else 7.5625 * (x - (1.5 / 2.75))**2 + 0.75 if x < 2 / 2.75 \
    else 7.5625 * (x - (2.25 / 2.75))**2 + 0.9375 if x < 2.5 / 2.75 else 7.5625 * (x - (2.625 / 2.75))**2 + 0.984375
BounceIn = lambda x: Reverse(BounceOut, x)
BounceInOut = lambda x: ToInOut(BounceIn, x)

ElasticOut = lambda x: math.pow(2, -10 * x) * math.sin((x * 0.075) * (2 * math.pi) / 0.3) + 1
ElasticIn = lambda x: Reverse(ElasticOut, x)
ElasticOutHalf = lambda x: math.pow(2, -10 * x) * math.sin((0.5 * x - 0.075) * (2 * math.pi) / 0.3) + 1
ElasticOutQuarter = lambda x: math.pow(2, -10 * x) * math.sin((0.025 * x - 0.075) * (2 * math.pi) / 0.3) + 1
ElasticInOut = lambda x: ToInOut(ElasticIn, x)

numToEasing = {
    0: Linear,
    1: QuadIn, 2: QuadOut,
    3: QuadIn, 4: QuadOut, 5: QuadInOut,
    6: CubicIn, 7: CubicOut, 8: CubicInOut,
    9: QuartIn,  10: QuartOut, 11: QuartInOut,
    12: QuintIn, 13: QuintOut, 14: QuintInOut,
    15: SineIn, 16: SineOut, 17: SineInOut,
    18: ExpoIn, 19: ExpoOut, 20: ExpoInOut,
    21: CircIn, 22: CircOut, 23: CircInOut,
    24: ElasticIn, 25: ElasticOut, 26: ElasticOutHalf, 27: ElasticOutQuarter, 28: ElasticInOut,
    29: BackIn, 30: BackOut, 31: BackInOut,
    32: BounceIn, 33: BounceOut, 34: BounceInOut
}
