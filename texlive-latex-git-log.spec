# revision 30983
# category Package
# catalog-ctan /support/latex-git-log
# catalog-date 2013-06-19 18:12:49 +0200
# catalog-license gpl3
# catalog-version 0.9
Name:		texlive-latex-git-log
Version:	0.9
Release:	2
Summary:	Typeset git log information
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latex-git-log
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-git-log.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-git-log.doc.tar.xz
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
%{_texmfdistdir}/scripts/latex-git-log/latex-git-log
%doc %{_mandir}/man1/latex-git-log.1*
%doc %{_texmfdistdir}/doc/man/man1/latex-git-log.man1.pdf
%doc %{_texmfdistdir}/doc/support/latex-git-log/README
%doc %{_texmfdistdir}/doc/support/latex-git-log/example-output.tex
%doc %{_texmfdistdir}/doc/support/latex-git-log/example.pdf
%doc %{_texmfdistdir}/doc/support/latex-git-log/example.tex
%doc %{_texmfdistdir}/doc/support/latex-git-log/po/de.po

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
