%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/fsnotify/fsnotify
%global goipath		github.com/fsnotify/fsnotify
%global forgeurl	https://github.com/fsnotify/fsnotify
Version:		1.8.0

%gometa

Summary:	Filesystem notifications for Go
Name:		golang-github-fsnotify

Release:	1
Source0:	https://github.com/fsnotify/fsnotify/archive/v%{version}/fsnotify-%{version}.tar.gz
URL:		https://github.com/fsnotify/fsnotify
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)

%description
Filesystem notifications for Go

%files
%{_bindir}/fsnotify

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n fsnotify-%{version}

%build
%gobuildroot
for cmd in $(ls -1 cmd) ; do
	%gobuild -o _bin/$cmd %{goipath}/cmd/$cmd
done

%install
%goinstall
for cmd in $(ls -1 _bin) ; do
	install -Dpm 0755 _bin/$cmd %{buildroot}%{_bindir}/$cmd
done


%check
%if %{with check}
%gochecks
%endif
