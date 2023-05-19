#!/bin/bash

# --------------------------------
#   Default settings and lists
# --------------------------------

COWSAY="/usr/games/cowsay"
WORKSPACE_FOLDER="/workspaces/xlightdata"


# --------------------------------
#   Functions
# --------------------------------

run_xlighdata() {
    cd "${WORKSPACE_FOLDER}/xlightdata.3.0.8"
    echo "\n*** Running Xlightdata ***\n"
    echo "Please visit http://localhost:6080 in your browser" | ${COWSAY}
    echo "\n"
    python2.7 xdata.py 
    cd ${WORKSPACE_FOLDER}
    echo "Press ENTER to close this terminal."
}

compile_all() {
    cd "${WORKSPACE_FOLDER}/xlightdata.3.0.8/src"
    echo "\n*** Compiling ***\n"
    sudo python2.7 -m compileall .
    sudo chown developer *.pyc
    cd ${WORKSPACE_FOLDER}
    echo "Mooo! All done!" | ${COWSAY}
}

clean_all() {
    cd "${WORKSPACE_FOLDER}/xlightdata.3.0.8/src"
    echo "\n*** Cleaning***\n"
    sudo rm *.pyc
    cd ${WORKSPACE_FOLDER}
    echo "Mooo! All clean!" | ${COWSAY}
}

launch_qt_designer() {
    cd ${WORKSPACE_FOLDER}
    echo "\n*** Launching Qt Designer ***\n"
    echo "Please visit http://localhost:6080 in your browser" | ${COWSAY}
    echo "\n"
    designer
    echo "Press ENTER to close this terminal."
}

print_usage() {
    printf "Usage: runTasks [OPTION]...\n"
    printf "Run useful development tasks.\n\n"
    printf "   -x, --xlightdata     Run Xlightdata.\n"
    printf "   -a, --compile-all    Compile all files in 'src' folder.\n"
    printf "   -c, --clean          Clean all .pyc files in 'src' folder.\n"
    printf "   -q, --qt-designer    Launch Qt Designer.\n"
}

# Parsing args
VALID_ARGS=$(getopt -o xacq --long xlighdata,compile-all,clean,qt-designer -- "$@")
if [ $? -ne 0 ]; then
    print_usage
    echo "Unknown parameter: $1" | ${COWSAY}
    exit 1;
fi

eval set -- "$VALID_ARGS"
while [ : ]; do
    case "$1" in
        -x | --xlightdata)
            run_xlighdata
            shift
            ;;
        -a | --compile-all)
            compile_all
            shift
            ;;
        -c | --clean)
            clean_all
            shift
            ;;
        -q | --qt-designer)
            launch_qt_designer
            shift
            ;;
        --) shift;
            break;
            ;;
    esac
done    

exit 0;

# while [[ "$#" -gt 0 ]]; do case $1 in
#     -x|--xlightdata) run_xlighdata; exit 0;;
#     -a|--compile-all) compile_all; exit 0;;
#     -c|--clean) clean_all; exit 0;;
#     -q|--qt-designer) launch_qt_designer; exit 0;;
#     *) print_usage; echo "Unknown parameter: $1" | ${COWSAY}; exit 1;; 
# esac; shift; done