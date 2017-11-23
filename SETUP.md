**Setting up philkr's fork of supertuxkart on a fresh Ubuntu installation**

(tested on Ubuntu 16.04 LTS running on a VirtualBox)

Update and install dependencies (many suggested by the supertuxkart GitHub readme)

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git python3-pip build-essential libssl-dev libffi-dev python-dev cmake libbluetooth-dev libcurl4-gnutls-dev libfreetype6-dev libfribidi-dev libgl1-mesa-dev libjpeg-dev libogg-dev libopenal-dev libpng-dev libvorbis-dev libxrandr-dev mesa-common-dev pkg-config zlib1g-dev python3-venv python3-tk
```

Create a virtualenv and install more dependencies

```
python3 -m venv nn
source nn/bin/activate
pip install tensorflow jupyter matplotlib
```

Clone the repository and get into `pykart`, where we'll be editing a file involved in CMake (I honestly don't really know how it all works but the error messages and StackOverflow were clear enough)

```
git clone https://github.com/philkr/supertuxkart.git
cd supertuxkart/pykart/
```

Find out where numpy is (while still in your virtualenv - check with `which python` and `which pip`)

```
python -c "import numpy; print(numpy.__file__)"
```

You'll get something like

```
/home/rainier/Desktop/nn/lib/python3.5/site-packages/numpy/__init__.py
```

That's where your virtualenv's Python executable (`which python`) looks for numpy when you import it.

`FindNumPy.cmake` is trying to set `PYTHON_NUMPY_INCLUDE_DIR`. If you do not follow the next step, `cmake` will fail to find this variable and terminate.

After line 31 of `FindNumPy.cmake` add a line like:

```
set(PYTHON_NUMPY_INCLUDE_DIR "/home/rainier/Desktop/nn/lib/python3.5/site-packages/numpy/core/include")
```

Go back to the `supertuxkart` root, make a `build` dir and build

```
cd ..
mkdir build
cd build
cmake ..
make -j9
```

Put the `supertuxkart` binary in `build/bin` in the pytux working directory

```
cp bin/supertuxkart ../pytux
```

And race

```
python __main__.py
```

