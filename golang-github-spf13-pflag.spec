# Run tests in check section
%bcond_without check

# https://github.com/spf13/pflag
%global goipath		github.com/spf13/pflag
%global forgeurl	https://github.com/spf13/pflag
Version:		1.0.5

%gometa

Summary:	Replacement for Go's flag package
Name:		golang-github-spf13-pflag

Release:	1
Source0:	https://github.com/spf13/pflag/archive/v%{version}/pflag-%{version}.tar.gz
URL:		https://github.com/spf13/pflag
License:	BSD with advertising
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
pflag is a drop-in replacement for Go's flag package,
implementing POSIX/GNU-style --flags.

pflag is compatible with the GNU extensions to the POSIX recommendations
for command-line options. For a more precise description,
see the "Command-line flag syntax" section below.

pflag is available under the same style of BSD license as the Go language,
which can be found in the LICENSE file.

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
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n pflag-%{version}

# workaround flag_test.go test with golang-1.18
sed -e 's/fmt.Println/fmt.Print/' -i flag_test.go

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

