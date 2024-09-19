toplevel_dir=`git rev-parse --show-toplevel`

echo "Root is - ${toplevel_dir}"

export PROJECT_ROOT=${toplevel_dir}

# Dirs variabless
export DSDL_OUTPUT=${PROJECT_ROOT}/common
export EXTERNAL_DIR=${PROJECT_ROOT}/external

# Python config
export PYTHONPATH=${DSDL_OUTPUT}:${PROJECT_SCRIPTS_ROOT}:$PYTHONPATH

# Yakut defaults
export YAKUT_FORMAT=json
export YAKUT_COMPILE_OUTPUT=${DSDL_OUTPUT}
export YAKUT_PATH=${YAKUT_COMPILE_OUTPUT}
# and some more in .bashrc


pushd . > /dev/null
cd $PROJECT_ROOT
# Any commands relative to top dir go here
popd > /dev/null

echo "Sourced all"
return 0
