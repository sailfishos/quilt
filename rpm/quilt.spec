Name:       quilt
Summary:    Scripts for working with series of patches
Version:    0.64
Release:    1
Group:      Development/Tools
License:    GPLv2+
URL:        https://github.com/sailfishos/recode
Source0:    %{name}-%{version}.tar.gz
Requires:   coreutils
Requires:   diffutils
Requires:   gzip
Requires:   bzip2
Requires:   sed
Requires:   gawk
Requires:   diffstat
Requires:   util-linux
Requires:   tar
Requires:   rpm-build
BuildRequires:  gettext-devel
BuildRequires:  gawk
BuildRequires:  util-linux

%description
These scripts allow one to manage a series of patches by keeping track of the
changes each patch makes. Patches can be applied, un-applied, refreshed, etc.

The scripts are heavily based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%configure \
    --with-diffstat=%{_bindir}/diffstat

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
export BUILD_ROOT=%{buildroot}
%make_install

rm -rf $RPM_BUILD_ROOT/%{_docdir}
%find_lang quilt

%files -f quilt.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO
%{_bindir}/guards
%{_bindir}/quilt
%dir %{_datadir}/quilt
%{_datadir}/quilt/*
%{_datadir}/emacs/site-lisp/quilt.el
%{_sysconfdir}/bash_completion.d/*
%config %{_sysconfdir}/quilt.quiltrc
%{_mandir}/man1/*

