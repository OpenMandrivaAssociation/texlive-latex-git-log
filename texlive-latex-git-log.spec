Name:		texlive-latex-git-log
Version:	71402
Release:	1
Summary:	Typeset git log information
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/latex-git-log
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-git-log.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-git-log.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-latex-git-log.bin = %{EVRD}

%description
The program is run within a git repository, and outputs the
entire version history, as a LaTeX table. That output will
typically be redirected to a file; the author recommends
typesetting in landscape orientation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latex-git-log
%{_texmfdistdir}/scripts/latex-git-log
%doc %{_mandir}/man1/*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/latex-git-log

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf ../share/texmf-dist/scripts/latex-git-log/latex-git-log latex-git-log
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
