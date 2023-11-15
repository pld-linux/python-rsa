%define		module	rsa
Summary:	Pure-Python RSA implementation
Summary(pl.UTF-8):	Czysto pythonowa implementacja RSA
Name:		python-%{module}
Version:	4.5
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/rsa/
Source0:	https://files.pythonhosted.org/packages/source/r/rsa/%{module}-%{version}.tar.gz
# Source0-md5:	f6d05e133e715d77b207bb7bd90d7854
URL:		https://pypi.org/project/rsa/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the commandline.

%description -l pl.UTF-8
Python-RSA to implementacja RSA w czystym Pythonie. Obsługuje
szyfrowanie i odszyfrowywanie, podpisywanie i sprawdzanie podpisów
oraz generowanie kluczy zgodnie z PKCS#1 w wersji 1.5. Moduł może być
używany jako biblioteka Pythona, jak i z linii poleceń.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

for f in $RPM_BUILD_ROOT%{_bindir}/pyrsa-* ; do
	%{__mv} "$f" "${f}-2"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt LICENSE README.md
%attr(755,root,root) %{_bindir}/pyrsa-decrypt-2
%attr(755,root,root) %{_bindir}/pyrsa-encrypt-2
%attr(755,root,root) %{_bindir}/pyrsa-keygen-2
%attr(755,root,root) %{_bindir}/pyrsa-priv2pub-2
%attr(755,root,root) %{_bindir}/pyrsa-sign-2
%attr(755,root,root) %{_bindir}/pyrsa-verify-2
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
