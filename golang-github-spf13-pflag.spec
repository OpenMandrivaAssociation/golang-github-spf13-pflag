# http://github.com/spf13/pflag
%global goipath         github.com/spf13/pflag
Version:                1.0.3

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Replacement for Go's flag package
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
pflag is a drop-in replacement for Go's flag package,
implementing POSIX/GNU-style --flags.

pflag is compatible with the GNU extensions to the POSIX recommendations
for command-line options. For a more precise description,
see the "Command-line flag syntax" section below.

pflag is available under the same style of BSD license as the Go language,
which can be found in the LICENSE file.

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
pflag is a drop-in replacement for Go's flag package,
implementing POSIX/GNU-style --flags.

pflag is compatible with the GNU extensions to the POSIX recommendations
for command-line options. For a more precise description,
see the "Command-line flag syntax" section below.

pflag is available under the same style of BSD license as the Go language,
which can be found in the LICENSE file.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%install
%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.3-1
- Update to release 1.0.3

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.0-5.gite57e3ee
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.gite57e3ee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-3.gite57e3ee
- Update to spec 3.0

* Fri Mar 02 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-2
- Autogenerate some parts using the new macros

* Wed Feb 21 2018 Kaushal <kshlster@gmail.com> - 1.0.0-1
- Update to upstream v1.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.gitc7e63cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.gitc7e63cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.18.gitc7e63cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitc7e63cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.gitc7e63cf
- Bump to upstream c7e63cf4530bcd3ba943729cee0efeff2ebea63f
  related: #1214731

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.git08b1a58
- Polish the spec file
  related: #1214731

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.git08b1a58
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.13.git08b1a58
- Bump to upstream 08b1a584251b5b62f458943640fc8ebd4d50aaa5
  related: #1214731

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.12.git5644820
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git5644820
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 12 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.10.git5644820
- Update spec file to spec-2.0
  related: #1214731

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git5644820
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.git5644820
- Bump to upstream 5644820622454e71517561946e3d94b9f9db6842
  related: #1214731

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.git18d831e
- Bump to upstream 18d831e92d67eafd1b0db8af9ffddbd04f7ae1f4
  resolves: #1214731

* Mon Mar 30 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git11b7cf8
- Bump to upstream 11b7cf8387a31f278486eaad758162830eca8c73
  related: #1085890

* Wed Feb 25 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git370c317
- Bump to upstream 370c3171201099fa6b466db45c8a032cbce33d8d
  related: #1085890

* Fri Feb 06 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitf82776d
- Bump to upstream f82776d6cc998e3c026baef7b24409ff49fe5c8d
  related: #1085890

* Thu Oct 16 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.git463bdc8
- Bump to 463bdc838f2b35e9307e91d480878bda5fff7232

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git94e98a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial package
