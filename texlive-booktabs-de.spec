Name:		texlive-booktabs-de
Version:	21907
Release:	2
Summary:	German version of booktabs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/booktabs-de
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the booktabs.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/booktabs-de/README-DE
%doc %{_texmfdistdir}/doc/latex/booktabs-de/booktabs-de.dtx
%doc %{_texmfdistdir}/doc/latex/booktabs-de/booktabs-de.ins
%doc %{_texmfdistdir}/doc/latex/booktabs-de/booktabs-de.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
