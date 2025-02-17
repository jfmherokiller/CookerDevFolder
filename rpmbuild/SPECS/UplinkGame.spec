Name:           UplinkGame
Version:        1
Release:        1%{?dist}
Summary:        Video Game
ExclusiveArch:      x86_64
Group: Game
License: IDK       
URL:     https://error.error       
Source0: https://archive.org/download/humble-introversion-bundle/Humble%20Introversion%20Bundle.zip/Humble%20Introversion%20Bundle%2FUplinkSource.tgz

BuildRequires: pkgconfig(freetype2)
BuildRequires: devel(libX11)
BuildRequires: devel(libXext)
BuildRequires: devel(libcairo)
BuildRequires: pkgconfig(SDL_mixer)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(xrandr)
BuildRequires: automake
BuildRequires: lib64glvnd-devel
Requires:  lib64freetype6   

%description
the hax

%prep
%autosetup -c -n "trunky"


%build
mv "Uplink Source" "Uplink"
cd "Uplink/trunk"
export UPLINKROOT=`pwd`
sed -i 's/CC = apgcc/CC = gcc/' $UPLINKROOT/standard.mk
sed -i 's/CXX = apg++/CXX = g++/' $UPLINKROOT/standard.mk
cd $UPLINKROOT/contrib
sed -i 's/CC=apgcc/CC = gcc/' Makefile
sed -i 's/CXX=apg++/CXX = g++/' Makefile

#freetype fixes
cd freetype-2.2.1
#fpermissive fixes for freetype
sed -i '662s/char/const char/g' src/base/ftrfork.c
sed -i '155s/char/const char/g' src/tools/apinames.c
#enter builds
cd builds/unix
wget -O config.guess 'https://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD'
wget -O config.sub 'https://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD'
cd ../../
#exit freetype builds
./autogen.sh
cd ..
#completely exit freetype

#sdl fixes
sed -i '571s/SDL_AllocAudioMem/(Uint8 *)SDL_AllocAudioMem/' $UPLINKROOT/contrib/SDL-1.2.11_dev/src/audio/SDL_audio.c
sed -i '163s/LONG64/false/'                                 $UPLINKROOT/contrib/SDL-1.2.11_dev/src/video/x11/SDL_x11sym.h
#end sdl fixes


make
cd $UPLINKROOT/lib
make
cd $UPLINKROOT/uplink/src
make
%configure
%make_build


%install
%make_install


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Mon Jan 20 06:28:00 UTC 2025 noah
- 
