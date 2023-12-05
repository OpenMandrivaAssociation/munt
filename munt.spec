%define major 2
%define libname %mklibname mt32emu %{major}
%define devname %mklibname mt32emu -d

%define tagversion %(echo %{version} | sed -e 's,\\\.,_,g')

Name: munt
Version: 2.7.0
Release: 1
Source0: https://github.com/munt/munt/archive/refs/tags/munt_%{tagversion}.tar.gz
Summary: Roland MT-32 emulator
URL: https://github.com/munt/munt
License: GPL
Group: Emulators
BuildRequires: cmake ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: qmake5
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(glib-2.0)

%description
Roland MT-32 emulator

The Roland MT-32 was a kind of external sound card connected via
MIDI, commonly used by DOS era games.

%package -n %{libname}
Summary: Roland MT-32 emulator
Group: System/Libraries

%description -n %{libname}
Roland MT-32 emulator

The Roland MT-32 was a kind of external sound card connected via
MIDI, commonly used by DOS era games.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n %{name}-%{name}_%{tagversion}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_datadir}/applications/mt32emu-qt.desktop
%{_datadir}/icons/hicolor/*/apps/munt.*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
