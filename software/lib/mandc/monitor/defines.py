KEY_SPLIT = "."
KEY_FORMAT_STRING = "{mclass}{ksp}{instance}{ksp}{group}{ksp}{attribute}"
KEY_ARG_FORMAT_STRING = KEY_SPLIT.join(["{key}", "{arg}"])

# IF / ethernet suffix
_IF_SUFFIX = "if%d"
_ETH_SUFFIX = "eth%d"
# 2-bit and 8-bit prefixes
_NBIT_PREFIX = "%dbit"
_2BIT_PREFIX = _NBIT_PREFIX % 2
_8BIT_PREFIX = _NBIT_PREFIX % 8

#################################### R2DBE monitor groups and attributes
R2DBE_MCLASS = "r2dbe"
# Snap data
R2DBE_GROUP_SNAP = "snap"
R2DBE_ATTR_SNAP_8BIT_COUNTS = "{b8}_counts".format(b8=_8BIT_PREFIX)
R2DBE_ARG_SNAP_8BIT_COUNTS = _IF_SUFFIX
R2DBE_ATTR_SNAP_8BIT_VALUES = "{b8}_values".format(b8=_8BIT_PREFIX)
R2DBE_ARG_SNAP_8BIT_VALUES = _IF_SUFFIX
R2DBE_ATTR_SNAP_2BIT_COUNTS = "{b2}_counts".format(b2=_2BIT_PREFIX)
R2DBE_ARG_SNAP_2BIT_COUNTS = _IF_SUFFIX
R2DBE_ATTR_SNAP_2BIT_VALUES = "{b2}_values".format(b2=_2BIT_PREFIX)
R2DBE_ARG_SNAP_2BIT_VALUES = _IF_SUFFIX
R2DBE_ATTR_SNAP_8BIT_DENSITY = "{b8}_spec".format(b8=_8BIT_PREFIX)
R2DBE_ARG_SNAP_8BIT_DENSITY = _IF_SUFFIX
R2DBE_ATTR_SNAP_8BIT_FREQUENCY = "{b8}_freq".format(b8=_8BIT_PREFIX)
R2DBE_ARG_SNAP_8BIT_FREQUENCY = _IF_SUFFIX
R2DBE_ATTR_SNAP_2BIT_DENSITY = "{b2}_spec".format(b2=_2BIT_PREFIX)
R2DBE_ARG_SNAP_2BIT_DENSITY = _IF_SUFFIX
R2DBE_ATTR_SNAP_2BIT_FREQUENCY = "{b2}_freq".format(b2=_2BIT_PREFIX)
R2DBE_ARG_SNAP_2BIT_FREQUENCY = _IF_SUFFIX
# FFT size
R2DBE_SNAP_FFT_SIZE = 4096
# Total power monitor
R2DBE_GROUP_POWER = "power"
R2DBE_ATTR_POWER_VALUES = "values"
R2DBE_ARG_POWER_VALUES = _IF_SUFFIX
R2DBE_ATTR_POWER_2BIT_THRESHOLD = "{b2}_threshold".format(b2=_2BIT_PREFIX)
R2DBE_ARG_POWER_2BIT_THRESHOLD = _IF_SUFFIX
# VDIF header
R2DBE_GROUP_VDIF = "vdif"
R2DBE_ATTR_VDIF_STATION = "station"
R2DBE_ARG_VDIF_STATION = _ETH_SUFFIX
R2DBE_ATTR_VDIF_POLARIZATION = "polarization"
R2DBE_ARG_VDIF_POLARIZATION = _ETH_SUFFIX
R2DBE_ATTR_VDIF_RECEIVER_SIDEBAND = "rx_sideband"
R2DBE_ARG_VDIF_RECEIVER_SIDEBAND = _ETH_SUFFIX
R2DBE_ATTR_VDIF_BDC_SIDEBAND = "bdc_sideband"
R2DBE_ARG_VDIF_BDC_SIDEBAND = _ETH_SUFFIX
# Time synchronization
R2DBE_GROUP_TIME = "time_synchronization"
R2DBE_ATTR_TIME_NOW = "current_time"
R2DBE_ATTR_TIME_GPS_PPS_COUNT = "gps_pps_count"
R2DBE_ATTR_TIME_GPS_PPS_OFFSET_TIME = "gps_pps_offset_seconds"
R2DBE_ATTR_TIME_GPS_PPS_OFFSET_CYCLE = "gps_pps_offset_clocks"
R2DBE_ATTR_TIME_ALIVE = "alive"
