CURRENT_DIR=$(pwd)
BUILD_DIR="/tmp/robot"
rm -rf $BUILD_DIR
mkdir $BUILD_DIR
cp -r robot $BUILD_DIR
cp scripts/pypi/robot/setup.py $BUILD_DIR/
cd $BUILD_DIR
python setup.py sdist
RELEASE=$(ls $BUILD_DIR/dist/)
echo "twine upload $BUILD_DIR/dist/$RELEASE"
cd $CURRENT_DIR

