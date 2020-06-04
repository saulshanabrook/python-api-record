
random = ...
abs = ...
testing = ...
r_ = ...
floating = ...
bool_ = ...
newaxis = ...
pi = ...
float = ...
bool = ...
int = ...
ogrid = ...
integer = ...
mgrid = ...
round = ...
float16 = ...
float_ = ...
nan = ...
min = ...
max = ...
double = ...
inf = ...
intp = ...
linalg = ...
divide = ...
signedinteger = ...
complex = ...
unsignedinteger = ...
__version__ = ...
int_ = ...
typecodes = ...
e = ...
c_ = ...
uint = ...
NaN = ...
ma = ...
NAN = ...
bitwise_xor = ...
complex64 = ...
s_ = ...
bool8 = ...
ubyte = ...

def arange(_0: Union[(numpy.int64, dask.array.core.Array, float, int, numpy.float64)], _0: Union[(numpy.int64, dask.array.core.Array, float, int, numpy.float64)]=..., /, *, dtype: Union[(list, list[int], list[numpy.int64], numpy.dtype)]=...):
    'usage.sample_usage: 4\nusage.skimage: 223'

def array(_0, _0=..., /, *, dtype=..., ndmin: int=..., copy: bool=..., order: Literal[('C', 'K', 'F')]=...):
    'usage.sample_usage: 1\nusage.skimage: 1076'

def zeros(_0, _0=..., /, *, dtype=..., order: Literal[('C', 'F')]=...):
    'usage.sample_usage: 1\nusage.skimage: 787'

def ones(shape, dtype=..., order: Literal[('F',)]=...):
    'usage.sample_usage: 1\nusage.skimage: 269'

def linspace(start: Union[(numpy.int64, float, numpy.float64, int)], stop: Union[(numpy.int64, float, numpy.float32, int, numpy.float64)], num: int, dtype: list=..., endpoint: bool=...):
    'usage.sample_usage: 1\nusage.skimage: 70'

def eye(N: int, M: int=..., dtype: list=...):
    'usage.sample_usage: 1\nusage.skimage: 39'

def add(_0: numpy.ndarray, _1: Union[(int, tuple[(int, int)], numpy.ndarray, tuple[(int, int, int)], float)], _0: numpy.ndarray=..., _1: Union[(int, tuple[(int, int)], numpy.ndarray, tuple[(int, int, int)], float)]=..., /, *, dtype: list=...):
    'usage.sample_usage: 1\nusage.skimage: 11'

def exp(_0: Union[(float, numpy.ndarray, int)], _0: Union[(float, numpy.ndarray, int)]=..., /, *, dtype: numpy.dtype=...):
    'usage.sample_usage: 1\nusage.skimage: 26'

def log(_0: Union[(dask.array.core.Array, float, int, numpy.ndarray, numpy.float64)], _0: Union[(dask.array.core.Array, float, int, numpy.ndarray, numpy.float64)]=..., /):
    'usage.sample_usage: 1\nusage.skimage: 19'

def column_stack(tup: Union[(list[numpy.ndarray], tuple[(numpy.ndarray, numpy.ndarray)])]):
    'usage.sample_usage: 1\nusage.skimage: 9'

def concatenate(_0, _0=..., /, *, axis: int=...):
    'usage.sample_usage: 1\nusage.skimage: 48'

def absolute(_0, _0=..., /):
    'usage.skimage: 113'

def asarray(a, dtype=..., order: Literal[('C',)]=...):
    'usage.skimage: 247'

def sum(a: Union[(numpy.ndarray, list[numpy.ndarray], tuple[(int, int, int)], tuple[(int, int)])], axis: Union[(tuple[(int, int)], int)]=...):
    'usage.skimage: 125'

def vstack(tup: Union[(tuple[(numpy.ndarray, numpy.ndarray, numpy.ndarray)], tuple[(numpy.ndarray, numpy.ndarray)], list[numpy.ndarray], tuple[(Union[(numpy.ndarray, list[Union[(float, int)]], list[numpy.int64])], Union[(numpy.ndarray, list[Union[(float, int)]], list[numpy.int64])])])]):
    'usage.skimage: 33'

def all(a: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)], axis: int=...):
    'usage.skimage: 113'

def round_(a, decimals: int=...):
    'usage.skimage: 30'

def asanyarray(a, dtype: list[bool]=...):
    'usage.skimage: 50'

def obj2sctype(rep):
    'usage.skimage: 14'

def issubdtype(arg1, arg2: list):
    'usage.skimage: 162'

def multiply(_0: numpy.ndarray, _1: Union[(numpy.ndarray, float, int)], _0: numpy.ndarray=..., _1: Union[(numpy.ndarray, float, int)]=..., /, *, out: numpy.ndarray=..., dtype: Union[(list, list[numpy.float64], list[numpy.float32], numpy.dtype)]=...):
    'usage.skimage: 25'

def reshape(a: Union[(numpy.ndarray, list[int])], newshape, order: Literal[('F',)]=...):
    'usage.skimage: 43'

def sqrt(_0, _0=..., /, *, out: numpy.ndarray=...):
    'usage.skimage: 112'

def moveaxis(a: numpy.ndarray, source: int, destination: int):
    'usage.skimage: 6'

def rollaxis(a: numpy.ndarray, axis: int, start: int=...):
    'usage.skimage: 14'

def any(a: Union[(numpy.ndarray, list[bool], numpy.bool_)]):
    'usage.skimage: 39'

def empty_like(_0: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)], _0: Union[(numpy.ndarray, numpy.ma.core.MaskedArray)]=..., /, *, dtype: list=..., subok: bool=..., order: Literal[('C',)]=...):
    'usage.skimage: 48'

def triu(m: numpy.ndarray):
    'usage.skimage: 1'

def seterr(invalid: Literal[('ignore', 'warn')], divide: Literal[('warn',)]=..., over: Literal[('warn',)]=..., under: Literal[('ignore',)]=...):
    'usage.skimage: 2'

def isnan(_0: Union[(numpy.ndarray, list[float], float)], _0: Union[(numpy.ndarray, list[float], float)]=..., /):
    'usage.skimage: 14'

def floor(_0: Union[(numpy.ndarray, numpy.float64, float)], _0: Union[(numpy.ndarray, numpy.float64, float)]=..., /):
    'usage.skimage: 13'

def stack(arrays, axis: int=...):
    'usage.skimage: 35'

def choose(a: numpy.ndarray, choices: list[numpy.ndarray]):
    'usage.skimage: 2'

def amin(a: Union[(numpy.ndarray, list[int], list[numpy.int64], tuple[(int, int)])], axis: Union[(tuple[(int, int)], int)]=...):
    'usage.skimage: 60'

def amax(a, axis: Union[(tuple[(int, int, int)], tuple[(int, int)], int)]=..., keepdims: bool=...):
    'usage.skimage: 105'

def rint(_0: numpy.ndarray, _0: numpy.ndarray=..., /, *, out: numpy.ndarray=None):
    'usage.skimage: 2'

def clip(a: Union[(numpy.ndarray, numpy.float64, int)], a_min, a_max, out: numpy.ndarray=...):
    'usage.skimage: 61'

def power(_0: Union[(numpy.ndarray, int)], _1: Union[(numpy.ndarray, float, int)], _0: Union[(numpy.ndarray, int)]=..., _1: Union[(numpy.ndarray, float, int)]=..., /):
    'usage.skimage: 11'

def log10(_0: Union[(numpy.ndarray, numpy.float64)], _0: Union[(numpy.ndarray, numpy.float64)]=..., /):
    'usage.skimage: 4'

def load(file: Literal[('/Users/saul/Downloads/scikit-image-0.17.0/skimage/',)]):
    'usage.skimage: 28'

def meshgrid(*xi: Literal[('v', 't')]):
    'usage.skimage: 28'

def dstack(tup: Union[(tuple[(numpy.ndarray, ...)], list[skimage.feature._hessian_det_appx._memoryviewslice], list[numpy.ndarray])]):
    'usage.skimage: 12'

def nonzero(a: numpy.ndarray):
    'usage.skimage: 22'

def cbrt(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
    'usage.skimage: 4'

def hypot(_0: Union[(numpy.ndarray, numpy.float64, int)], _1: Union[(numpy.ndarray, numpy.float64, int)], _0: Union[(numpy.ndarray, numpy.float64, int)]=..., _1: Union[(numpy.ndarray, numpy.float64, int)]=..., /):
    'usage.skimage: 13'

def arctan2(_0: Union[(numpy.ndarray, numpy.float64, numpy.int64)], _1: Union[(numpy.ndarray, numpy.float64, numpy.int64)], _0: Union[(numpy.ndarray, numpy.float64, numpy.int64)]=..., _1: Union[(numpy.ndarray, numpy.float64, numpy.int64)]=..., /):
    'usage.skimage: 8'

def where(_0: Union[(numpy.ndarray, dask.array.core.Array, numpy.bool_)], _0: Union[(numpy.ndarray, dask.array.core.Array, numpy.bool_)]=..., _1: Union[(numpy.ndarray, numpy.float64, float)]=..., _2: Union[(numpy.ndarray, numpy.float64, int)]=..., /):
    'usage.skimage: 26'

def cos(_0: Union[(numpy.ndarray, numpy.float64, float, int)], _0: Union[(numpy.ndarray, numpy.float64, float, int)]=..., /):
    'usage.skimage: 48'

def sin(_0: Union[(numpy.ndarray, numpy.float64, float, int)], _0: Union[(numpy.ndarray, numpy.float64, float, int)]=..., /):
    'usage.skimage: 47'

def ascontiguousarray(a: Union[(numpy.ndarray, list[float], list[Union[(float, int)]], list[int])], dtype: Union[(list[bool], list, numpy.dtype)]=...):
    'usage.skimage: 67'

def swapaxes(a: numpy.ndarray, axis1: int, axis2: int):
    'usage.skimage: 4'

def ravel(a):
    'usage.skimage: 12'

def squeeze(a: numpy.ndarray, axis: int=...):
    'usage.skimage: 16'

def ones_like(a: numpy.ndarray, dtype: list=...):
    'usage.skimage: 26'

def can_cast(_0: Union[(numpy.ndarray, float, int, numpy.dtype)], _1: Union[(list[bool], numpy.dtype)], _0: Union[(numpy.ndarray, float, int, numpy.dtype)]=..., _1: Union[(list[bool], numpy.dtype)]=..., /, *, casting: Literal[('safe',)]=...):
    'usage.skimage: 9'

def empty(_0, _0=..., /, *, dtype=..., order: Literal[('C', 'F')]=...):
    'usage.skimage: 129'

def min_scalar_type(_0: Union[(numpy.float64, numpy.int64, int)], _0: Union[(numpy.float64, numpy.int64, int)]=..., /):
    'usage.skimage: 5'

def unique(ar: numpy.ndarray, return_inverse: bool=..., return_counts: bool=..., return_index: bool=...):
    'usage.skimage: 68'

def zeros_like(a: Union[(numpy.ndarray, tuple[(int, int, int)], tuple[(int, int)])], dtype: list=..., order: Literal[('C',)]=...):
    'usage.skimage: 70'

def full(shape: Union[(numpy.ndarray, int, tuple[(int, ...)], tuple[(int,)], tuple[(int, int)])], fill_value, dtype=...):
    'usage.skimage: 36'

def loadtxt(fname: Literal[('/Users/saul/Downloads/scikit-image-0.17.0/skimage/',)], dtype: list[tuple[(Literal[('pair', 'b1', '1', 'a1', 'L1')], list)]]):
    'usage.skimage: 1'

def logical_and(_0: Union[(numpy.ndarray, numpy.bool_)], _1: Union[(numpy.ndarray, numpy.bool_)], _0: Union[(numpy.ndarray, numpy.bool_)]=..., _1: Union[(numpy.ndarray, numpy.bool_)]=..., /):
    'usage.skimage: 13'

def deg2rad(_0: Union[(numpy.ndarray, int, list[int])], _0: Union[(numpy.ndarray, int, list[int])]=..., /):
    'usage.skimage: 18'

def rad2deg(_0: Union[(numpy.ndarray, numpy.float64)], _0: Union[(numpy.ndarray, numpy.float64)]=..., /):
    'usage.skimage: 6'

def maximum(_0: Union[(numpy.ndarray, int, tuple[(int, int, int)], tuple[(int, int)], numpy.float64)], _1: Union[(numpy.ndarray, tuple[(int, int, int)], tuple[(int, int)], int)], _0: Union[(numpy.ndarray, int, tuple[(int, int, int)], tuple[(int, int)], numpy.float64)]=..., _1: Union[(numpy.ndarray, tuple[(int, int, int)], tuple[(int, int)], int)]=..., /, *, out: numpy.ndarray=..., casting: Literal[('unsafe',)]=..., dtype: numpy.dtype=...):
    'usage.skimage: 16'

def percentile(a: numpy.ndarray, q: Union[(int, float, list[int])]):
    'usage.skimage: 11'

def logical_not(_0: numpy.ndarray, _0: numpy.ndarray=..., /, *, out: numpy.ndarray=...):
    'usage.skimage: 14'

def isscalar(element):
    'usage.skimage: 67'

def ceil(_0: Union[(numpy.ndarray, int, float, numpy.float64, numpy.int64)], _0: Union[(numpy.ndarray, int, float, numpy.float64, numpy.int64)]=..., /):
    'usage.skimage: 31'

def minimum(_0: Union[(numpy.ndarray, tuple[(int, int, int)], tuple[(int, int)])], _1: Union[(numpy.ndarray, float, tuple[(int, int, int)], tuple[(int, int)])], _0: Union[(numpy.ndarray, tuple[(int, int, int)], tuple[(int, int)])]=..., _1: Union[(numpy.ndarray, float, tuple[(int, int, int)], tuple[(int, int)])]=..., /):
    'usage.skimage: 9'

def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
    'usage.skimage: 1'

def diag(v: numpy.ndarray):
    'usage.skimage: 5'

def arcsin(_0: float, /):
    'usage.skimage: 1'

def ellipkinc(_0: numpy.float64, _1: float, /):
    'usage.skimage: 1'

def ellipeinc(_0: numpy.float64, _1: float, /):
    'usage.skimage: 1'

def transpose(a, axes: Union[(tuple[(int, int, int, int)], tuple[(int, int, int)], numpy.ndarray, list[int])]=...):
    'usage.skimage: 21'

def shape(a: numpy.ndarray):
    'usage.skimage: 1'

def promote_types(_0: numpy.dtype, _1: numpy.dtype, /):
    'usage.skimage: 1'

def bincount(_0: Union[(numpy.ndarray, dask.array.core.Array)], _0: Union[(numpy.ndarray, dask.array.core.Array)]=..., /, *, minlength: int=...):
    'usage.skimage: 12'

def histogram(a: numpy.ndarray, bins: Union[(tuple[(numpy.float64, numpy.float64, numpy.float64, numpy.float64, numpy.float64)], list[Union[(float, int)]], numpy.int64, int)], density: bool=..., range: Union[(tuple[(int, int)], None)]=...):
    'usage.skimage: 7'

def interp(x: Union[(numpy.ndarray, numpy.flatiter)], xp: numpy.ndarray, fp: numpy.ndarray):
    'usage.skimage: 6'

def polyfit(x: numpy.ndarray, y: numpy.ndarray, deg: int):
    'usage.skimage: 1'

def pad(array: Union[(numpy.ndarray, list[int], list[list[int]])], pad_width, mode: Union[(Literal[('constant',)], Callable, Literal[('mean',)], Literal[('maximum', 'linear_ramp', 'minimum', 'reflect', 'symmetric', 'wrap', 'edge', 'constant', 'median', 'mean')], Literal[('edge',)])]=...):
    'usage.skimage: 126'

def product(*args: Literal[('v', 't')]):
    'usage.skimage: 14'

def apply_along_axis(func1d: Callable, axis: int, arr: numpy.ndarray):
    'usage.skimage: 8'

def count_nonzero(a: numpy.ndarray):
    'usage.skimage: 9'

def cumsum(a: Union[(numpy.ndarray, dask.array.core.Array)], axis: int=..., out: numpy.ndarray=...):
    'usage.skimage: 29'

def take_along_axis(arr: numpy.ndarray, indices: numpy.ndarray, axis: int):
    'usage.skimage: 1'

def square(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
    'usage.skimage: 7'

def mean(a: Union[(numpy.ndarray, dask.array.core.Array, list[numpy.float64])], axis: Union[(tuple[(int, int)], int)]=..., dtype: list=...):
    'usage.skimage: 61'

def log2(_0: Union[(numpy.ndarray, int)], _0: Union[(numpy.ndarray, int)]=..., /):
    'usage.skimage: 5'

def allclose(a: Union[(numpy.ndarray, list[numpy.float64], list[int], numpy.float64)], b, rtol: Union[(float, int)]=..., atol: float=...):
    'usage.skimage: 33'

def argsort(a: Union[(numpy.ndarray, numpy.flatiter)]):
    'usage.skimage: 28'

def hstack(tup):
    'usage.skimage: 27'

def argmax(a: Union[(numpy.ndarray, dask.array.core.Array)], axis: int=...):
    'usage.skimage: 18'

def logspace(start: Union[(numpy.float64, float)], stop: Union[(numpy.float64, float)], num: int):
    'usage.skimage: 2'

def logical_or(_0: numpy.ndarray, _1: numpy.ndarray, /):
    'usage.skimage: 3'

def isinf(_0: float, /):
    'usage.skimage: 2'

def delete(arr: numpy.ndarray, obj: tuple[(Union[(None, int)], ...)], axis: int):
    'usage.skimage: 3'

def split(ary: numpy.ndarray, indices_or_sections: int):
    'usage.skimage: 1'

def atleast_1d(*arys: Literal[('v', 't')]):
    'usage.skimage: 11'

def isclose(a: Union[(numpy.ndarray, numpy.float64, float)], b: Union[(float, int)], atol: float=...):
    'usage.skimage: 3'

def gradient(f: numpy.ndarray):
    'usage.skimage: 8'

def argmin(a: Union[(numpy.ndarray, list[numpy.float64])], axis: int=...):
    'usage.skimage: 10'

def arctan(_0: Union[(numpy.ndarray, numpy.float64)], _0: Union[(numpy.ndarray, numpy.float64)]=..., /):
    'usage.skimage: 3'

def sort(a: numpy.ndarray, axis: int=...):
    'usage.skimage: 14'

def spacing(_0: int, /):
    'usage.skimage: 1'

def isfinite(_0: Union[(numpy.ndarray, list[Union[(numpy.float64, numpy.int64)]], tuple[(numpy.ndarray, numpy.ndarray)])], _0: Union[(numpy.ndarray, list[Union[(numpy.float64, numpy.int64)]], tuple[(numpy.ndarray, numpy.ndarray)])]=..., /):
    'usage.skimage: 7'

def diff(a: numpy.ndarray, n: int=..., axis: int=...):
    'usage.skimage: 15'

def flatnonzero(a: numpy.ndarray):
    'usage.skimage: 6'

def copy(a: Union[(numpy.ndarray, numpy.float64)]):
    'usage.skimage: 14'

def atleast_2d(*arys: Literal[('v', 't')]):
    'usage.skimage: 7'

def rot90(m: numpy.ndarray, k: int=...):
    'usage.skimage: 7'

def roll(a: Union[(numpy.ndarray, list[Union[(float, int)]])], shift: Union[(tuple[(int, int)], int)], axis: Union[(tuple[(int, int)], int)]=...):
    'usage.skimage: 14'

def indices(dimensions: tuple[(Union[(numpy.int64, int)], ...)], dtype: list[numpy.float64]=...):
    'usage.skimage: 6'

def tri(N: int, M: int=..., k: int=..., dtype: list[numpy.int32]=...):
    'usage.skimage: 9'

def less(_0: tuple[(int, ...)], _1: tuple[(int, ...)], _0: tuple[(int, ...)]=..., _1: tuple[(int, ...)]=..., /):
    'usage.skimage: 3'

def prod(a: Union[(numpy.ndarray, tuple[(int, ...)], list[int])]):
    'usage.skimage: 9'

def true_divide(_0: numpy.ndarray, _1: Union[(numpy.ndarray, numpy.int64)], _0: numpy.ndarray=..., _1: Union[(numpy.ndarray, numpy.int64)]=..., /, *, out: numpy.ndarray=...):
    'usage.skimage: 2'

def unravel_index(_0: Union[(numpy.ndarray, numpy.int64, int)], _1: tuple[(int, ...)], _0: Union[(numpy.ndarray, numpy.int64, int)]=..., _1: tuple[(int, ...)]=..., /):
    'usage.skimage: 18'

def apply_over_axes(func: Callable, a: numpy.ndarray, axes: tuple[(int, int)]):
    'usage.skimage: 10'

def tile(A: Union[(numpy.ndarray, tuple[(int, int)], list[int])], reps: Union[(tuple[(int, int, int, int)], tuple[(int, int)], tuple[(int, ...)], list[int])]):
    'usage.skimage: 15'

def real(val: Union[(numpy.ndarray, float)]):
    'usage.skimage: 8'

def imag(val: numpy.ndarray):
    'usage.skimage: 1'

def sign(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
    'usage.skimage: 4'

def subtract(_0: int, _1: numpy.ndarray, _0: int=..., _1: numpy.ndarray=..., /, *, dtype: numpy.dtype=None):
    'usage.skimage: 11'

def ix_(*args: Literal[('v', 't')]):
    'usage.skimage: 2'

def convolve(a: numpy.ndarray, v: list[float], mode: Literal[('valid',)]):
    'usage.skimage: 1'

def invert(_0: Union[(numpy.ndarray, list[bool])], _0: Union[(numpy.ndarray, list[bool])]=..., /):
    'usage.skimage: 7'

def array_equal(a1: Union[(numpy.ndarray, tuple[(float, float, float)], list[int])], a2: Union[(numpy.ndarray, tuple[(int, int, int)])]):
    'usage.skimage: 5'

def reciprocal(_0: numpy.ndarray, /, *, out: numpy.ndarray=None):
    'usage.skimage: 1'

def insert(arr: numpy.ndarray, obj: int, values: numpy.ndarray, axis: int):
    'usage.skimage: 3'

def full_like(a: numpy.ndarray, fill_value: int):
    'usage.skimage: 1'

def sctype2char(sctype: numpy.dtype):
    'usage.skimage: 2'

def floor_divide(_0: numpy.ndarray, _1: int, _0: numpy.ndarray=..., _1: int=..., /, *, out: numpy.ndarray=None, dtype: numpy.dtype=None, casting: Literal[('unsafe',)]=None):
    'usage.skimage: 4'

def fromfile(_0: _io.TextIOWrapper, /, *, sep: Literal[(' ',)]=None):
    'usage.skimage: 1'

def median(a: numpy.ndarray, axis: tuple[(int, int)]=...):
    'usage.skimage: 5'

def asfortranarray(a: numpy.ndarray):
    'usage.skimage: 1'

def cross(a: numpy.ndarray, b: numpy.ndarray):
    'usage.skimage: 5'

def einsum(*operands: Literal[('v', 't')]):
    'usage.skimage: 1'

def nan_to_num(x: list[numpy.float64]):
    'usage.skimage: 1'

def frombuffer(_0: bytes, /, *, dtype: Literal[('int8',)]=None):
    'usage.skimage: 1'

def fliplr(m: numpy.ndarray):
    'usage.skimage: 5'

def tril(m: numpy.ndarray):
    'usage.skimage: 1'

def flip(m: numpy.ndarray, axis: int):
    'usage.skimage: 3'

def flipud(m: numpy.ndarray):
    'usage.skimage: 2'

def set_printoptions(precision: int):
    'usage.skimage: 1'

def result_type(_0: numpy.dtype, _1: numpy.dtype, _2: list[numpy.float32], _0: numpy.dtype=..., _1: numpy.dtype=..., _2: list[numpy.float32]=..., /):
    'usage.skimage: 7'

def ptp(a: numpy.ndarray):
    'usage.skimage: 10'

def cumprod(a: tuple[(int, ...)]):
    'usage.skimage: 5'

def ravel_multi_index(_0, _1: tuple[(int, ...)], _0=..., _1: tuple[(int, ...)]=..., /, *, order: Literal[('C', 'F')]=...):
    'usage.skimage: 18'

def logical_xor(_0: numpy.ndarray, _1: numpy.ndarray, /, *, out: numpy.ndarray=None):
    'usage.skimage: 1'

def in1d(ar1: Union[(numpy.ndarray, numpy.flatiter)], ar2: Union[(numpy.ndarray, tuple[(int, int)])]):
    'usage.skimage: 2'

def take(a: numpy.ndarray, indices: numpy.ndarray):
    'usage.skimage: 1'

def lexsort(_0: tuple[(numpy.ndarray, numpy.ndarray, numpy.ndarray)], /):
    'usage.skimage: 1'

def fmax(_0: numpy.ndarray, _1: Union[(numpy.float64, float)], _0: numpy.ndarray=..., _1: Union[(numpy.float64, float)]=..., /):
    'usage.skimage: 3'

def fix(x: Union[(numpy.float64, float)]):
    'usage.skimage: 2'

def tensordot(a: numpy.ndarray, b: numpy.ndarray, axes: tuple[(int, int)]):
    'usage.skimage: 1'

def atleast_3d(*arys: Literal[('v', 't')]):
    'usage.skimage: 11'

def iscomplexobj(x: numpy.ndarray):
    'usage.skimage: 4'

def conjugate(_0: numpy.ndarray, /):
    'usage.skimage: 2'

def angle(z: numpy.ndarray):
    'usage.skimage: 3'

def require(a: numpy.ndarray, dtype: list[numpy.uint8], requirements: list[Literal[('C',)]]):
    'usage.skimage: 1'

def tanh(_0: numpy.ndarray, /):
    'usage.skimage: 2'

def ndim(a: numpy.ndarray):
    'usage.skimage: 4'

def searchsorted(a: numpy.ndarray, v: Union[(numpy.float64, int)]):
    'usage.skimage: 3'

def fill_diagonal(a: numpy.ndarray, val: float):
    'usage.skimage: 1'

def array2string(a: numpy.ndarray, separator: Literal[(', ',)]):
    'usage.skimage: 1'

def std(a: numpy.ndarray):
    'usage.skimage: 1'

def hamming(M: int):
    'usage.skimage: 1'

def hanning(M: int):
    'usage.skimage: 1'

def around(a: tuple[(numpy.float64, numpy.float64)]):
    'usage.skimage: 1'

def alltrue(*args: Literal[('v', 't')]):
    'usage.skimage: 2'

def may_share_memory(_0: numpy.ndarray, _1: numpy.ndarray, /):
    'usage.skimage: 2'

class ndarray():

    @classmethod
    def mean(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.sample_usage: 1\nusage.skimage: 23'

    @classmethod
    def sum(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.sample_usage: 1\nusage.skimage: 86'

    @classmethod
    def sort(_0: numpy.ndarray, /):
        'usage.sample_usage: 1'

    @classmethod
    def reshape(_0: numpy.ndarray, _1, _0: numpy.ndarray=..., _1=..., /):
        'usage.sample_usage: 2\nusage.skimage: 168'

    @classmethod
    def astype(_0: numpy.ndarray, _1, _0: numpy.ndarray=..., _1=..., /):
        'usage.sample_usage: 1\nusage.skimage: 555'

    @classmethod
    def copy(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 135'

    @classmethod
    def max(_0: numpy.ndarray, _0: numpy.ndarray=..., _1: int=..., /):
        'usage.skimage: 108'

    @classmethod
    def ptp(_0: numpy.ndarray, _0: numpy.ndarray=..., _1: int=..., /):
        'usage.skimage: 5'

    @classmethod
    def min(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 80'

    @classmethod
    def any(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 11'

    @classmethod
    def nonzero(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 4'

    @classmethod
    def fill(_0: numpy.ndarray, _1: Union[(bool, int)], _0: numpy.ndarray=..., _1: Union[(bool, int)]=..., /):
        'usage.skimage: 5'

    @classmethod
    def flatten(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 16'

    @classmethod
    def ravel(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 207'

    @classmethod
    def cumsum(_0: numpy.ndarray, /):
        'usage.skimage: 1'

    @classmethod
    def transpose(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 5'

    @classmethod
    def argmin(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 2'

    @classmethod
    def view(_0: numpy.ndarray, _0: numpy.ndarray=..., _1: Union[(list[bool], list[numpy.uint8], Literal[('|S16',)])]=..., /):
        'usage.skimage: 22'

    @classmethod
    def swapaxes(_0: numpy.ndarray, _1: int, _2: int, /):
        'usage.skimage: 2'

    @classmethod
    def argsort(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 5'

    @classmethod
    def argmax(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 6'

    @classmethod
    def std(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 63'

    @classmethod
    def all(_0: numpy.ndarray, /):
        'usage.skimage: 1'

    @classmethod
    def tobytes(_0: numpy.ndarray, _0: numpy.ndarray=..., /):
        'usage.skimage: 2'

    @classmethod
    def tolist(_0: numpy.ndarray, /):
        'usage.skimage: 1'

    @classmethod
    def dot(_0: numpy.ndarray, _1: numpy.ndarray, /):
        'usage.skimage: 1'

    @classmethod
    def conj(_0: numpy.ndarray, /):
        'usage.skimage: 4'
    shape: Union[(tuple[(int, int)], tuple[(int, ...)], numpy.ndarray, tuple[(int,)])] = ...
    ndim = ...
    dtype = ...
    size = ...
    T = ...
    flags = ...
    flat: numpy.ndarray = ...
    itemsize = ...
    strides: tuple[(int, int, int)] = ...

    def __iter__(self, /):
        ''

    def sort(self, /, *, axis: int=..., order: Literal[('accumulator',)]=...):
        'usage.sample_usage: 1\nusage.skimage: 9'

    def mean(self, /, *, axis: Union[(tuple[(int, int, int)], int)]=...):
        'usage.skimage: 28'

    def sum(self, /, *, axis: int=...):
        'usage.skimage: 23'

    def all(self, /):
        'usage.skimage: 47'

    def any(self, /):
        'usage.skimage: 4'

    def min(self, /):
        'usage.skimage: 18'

    def max(self, /):
        'usage.skimage: 18'

    def cumsum(self, /, *, axis: int=None):
        'usage.skimage: 6'

    def argmax(self, /, *, axis: int=None):
        'usage.skimage: 1'

    def astype(self, _0: Union[(list[numpy.uint8], list, list[numpy.int16], numpy.dtype)], _0: Union[(list[numpy.uint8], list, list[numpy.int16], numpy.dtype)]=..., /, *, copy: bool=...):
        'usage.skimage: 34'

    def tolist(self, /):
        'usage.skimage: 6'

    def std(self, /, *, axis: int=...):
        'usage.skimage: 2'

    def view(self, /, *, dtype: list[numpy.uint8]=None):
        'usage.skimage: 4'

    def clip(self, /, *, min: int=..., max: tuple[(int, ...)]=...):
        'usage.skimage: 3'

    def repeat(self, _0: int, /, *, axis: int=None):
        'usage.skimage: 2'

    def ravel(self, /):
        'usage.skimage: 2'

    def var(self, /, *, axis: int=...):
        'usage.skimage: 7'

class dtype():

    def __init__(_0, _0=..., /):
        'usage.sample_usage: 1\nusage.skimage: 19'
    type = ...
    kind = ...
    itemsize = ...
    name = ...
    char = ...

class ufunc():

    @classmethod
    def reduce(_0: Callable, _1: Union[(numpy.ndarray, list[numpy.ndarray], tuple[(int,)])], _0: Callable=..., _1: Union[(numpy.ndarray, list[numpy.ndarray], tuple[(int,)])]=..., /):
        'usage.sample_usage: 1\nusage.skimage: 6'

class float64():

    def __init__(x: Union[(numpy.ndarray, float, int, numpy.int64)], x: Union[(numpy.ndarray, float, int, numpy.int64)]=..., /):
        'usage.skimage: 8'
    ndim = ...
    shape = ...

class generic():

    @classmethod
    def astype(_0, _1: list[numpy.int64], _0=..., _1: list[numpy.int64]=..., /):
        'usage.skimage: 12'

    @classmethod
    def conj(_0: numpy.complex128, /):
        'usage.skimage: 1'

class iinfo():

    def __init__(int_type: Union[(list, numpy.dtype)]):
        'usage.skimage: 33'
    min = ...
    max = ...

class finfo():

    def __init__(dtype: numpy.dtype):
        'usage.skimage: 1'
    eps = ...
    resolution = ...
    max = ...
    min = ...

class flatiter():

    def __iter__(self, /):
        ''

class flagsobj():
    writeable: bool = ...
    f_contiguous = ...
    c_contiguous = ...

class ndindex():

    def __init__(*shape: Literal[('v', 't')]):
        'usage.skimage: 1'

    def __iter__(self, /):
        ''

class uint8():

    def __init__(_0: Union[(numpy.ndarray, numpy.float64, numpy.int64, int)], _0: Union[(numpy.ndarray, numpy.float64, numpy.int64, int)]=..., /):
        'usage.skimage: 6'

class int64():

    def __init__(_0: Union[(numpy.float64, numpy.int64)], _0: Union[(numpy.float64, numpy.int64)]=..., /):
        'usage.skimage: 2'
    ndim = ...

class float32():

    def __init__(_0: Union[(numpy.ndarray, int)], _0: Union[(numpy.ndarray, int)]=..., /):
        'usage.skimage: 4'

class matrix():
    A = ...

class complex128():
    imag = ...
    real = ...

class nditer():
    multi_index = ...

    def __iter__(self, /):
        ''

class int32():

    def __init__(_0: numpy.int64, /):
        'usage.skimage: 1'

class int8():

    def __init__(_0: Union[(numpy.ndarray, numpy.int64)], _0: Union[(numpy.ndarray, numpy.int64)]=..., /):
        'usage.skimage: 5'

class int16():

    def __init__(_0: Union[(numpy.int64, int)], _0: Union[(numpy.int64, int)]=..., /):
        'usage.skimage: 2'

class longlong():

    def __init__(_0: numpy.int64, /):
        'usage.skimage: 1'

class uint16():

    def __init__(_0: Union[(numpy.int64, int)], _0: Union[(numpy.int64, int)]=..., /):
        'usage.skimage: 2'

class uint32():

    def __init__(_0: numpy.int64, /):
        'usage.skimage: 1'

class uint64():

    def __init__(_0: numpy.int64, /):
        'usage.skimage: 1'

class ulonglong():

    def __init__(_0: numpy.int64, /):
        'usage.skimage: 1'