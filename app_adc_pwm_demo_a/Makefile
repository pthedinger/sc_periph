# The TARGET variable determines what target system the application is
# compiled for. It either refers to an XN file in the source directories
# or a valid argument for the --target option when compiling
TARGET = SLICEKIT-A16

# The APP_NAME variable determines the name of the final .xe file. It should
# not include the .xe postfix. If left blank the name will default to
# the project name
APP_NAME = 

# The USED_MODULES variable lists other module used by the application.
USED_MODULES = module_analog_tile_support module_logging module_pwm_tutorial_example module_xassert

# The flags passed to xcc when building the application
# You can also set the following to override flags for a particular language:
# XCC_XC_FLAGS, XCC_C_FLAGS, XCC_ASM_FLAGS, XCC_CPP_FLAGS
# If the variable XCC_MAP_FLAGS is set it overrides the flags passed to
# xcc for the final link (mapping) stage.
XCC_FLAGS_Debug = -O0 -g -fxscope
XCC_FLAGS_Release = -O2 -g -fxscope

# The VERBOSE variable, if set to 1, enables verbose output from the make system.
VERBOSE = 0

# This change to the module path is so that this application can be in the
# tests sub-directory in it's git repo
ifeq ($(notdir $(abspath ..)),tests)
PATHSEP = $(if $(findstring Windows, $(OS))$(findstring WINDOWS,$(OS)),;,:)
XMOS_MODULE_PATH := $(XMOS_MODULE_PATH)$(PATHSEP)../../..
endif

XMOS_MAKE_PATH ?= ../..
-include $(XMOS_MAKE_PATH)/xcommon/module_xcommon/build/Makefile.common
