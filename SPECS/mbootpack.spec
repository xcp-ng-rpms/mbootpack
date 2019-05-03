Name:          mbootpack
License:       GPL
Group:         System Environment/Base
Version:       v0.7a
Release:       1%{?dist}
Summary:       Multiboot image builder

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/mbootpack/archive?at=v0.7a&prefix=mbootpack-v0.7a&format=tgz#/mbootpack-v0.7a.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/mbootpack/archive?at=v0.7a&prefix=mbootpack-v0.7a&format=tgz#/mbootpack-v0.7a.tar.gz) = 190be011b093b616af0fe7f0e01ba10f11b47fed

BuildRequires: gcc

%description
This is a utility to take a multiboot kernel and modules and repackage
them in a form that a standard linux bootloader will be able to load them.

%prep
%autosetup -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
%{?cov_wrap} %{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}/%{_bindir}
%{__install} -s %{name} %{buildroot}/%{_bindir}

%files
%doc README GPL
%{_bindir}/%{name}

%changelog
