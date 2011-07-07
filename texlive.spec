# This spec file is based on texjive project created by Michael A. Peters.
# Adopted and modified for Fedora by Jindrich Novy.

%define texlive_ver	2007
%define ptex_src_ver	3.1.10
%define pdvipsk_ver	p1.7a
%define mendexk_ver	2.6e

%define desktop_file_utils_version 0.9
%define default_letter_paper 0
# lcdf typetools can be easily built as a separate tool, so it should be
%define disable_lcdf_typetools 1

# These need to match what is in the texlive-texmf package.
#  since texlive-texmf is a BuildRequires, it installs an rpm macro
#  file that defines them. Change the definitions in the texlive-texmf.spec
#  file and rebuild it if you do not like where things get put.
%{!?_texmf_main: %define _texmf_main %{_datadir}/texmf}
%{!?_texmf_conf: %define _texmf_conf %{_sysconfdir}/texmf}
%{!?_texmf_var:  %define _texmf_var %{_var}/lib/texmf}

Name:		texlive
Version:	%{texlive_ver}
Release:	56%{?dist}
Summary:	Binaries for the TeX formatting system

Group:		Applications/Publishing
License:	GPLv2 and BSD and Public Domain and LGPLv2+ and GPLv2+ and LPPL
URL:		http://tug.org/texlive/

#####
# Source0-99: main sources
#####
#Source0:	http://tug.org/svn/texlive/branches/branch2007/Master/source/source.tar.bz2
# non free source files removed with texlive-generate-tarball.sh
Source0:	source-free.tar.bz2
# LGPL for kpathsea
Source1:	http://www.gnu.org/licenses/lgpl.txt

# Filter out bad requirements (RH bug #59819).
Source99:	texlive-filter-requires.sh
Source100:	texlive-generate-tarball.sh
%define __perl_requires %{SOURCE99}
# 1000-: Japanese pTeX
Source1000:	ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/tetex/ptex-src-%{ptex_src_ver}.tar.gz
Source1001:	ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/dvips/dvipsk-jpatch-%{pdvipsk_ver}.tar.gz
Source1002:	ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/mendex/mendexk%{mendexk_ver}.tar.gz

# Don't run brp-python-bytecompile
%define __os_install_post  /usr/lib/rpm/brp-compress /usr/lib/rpm/brp-strip %{__strip} /usr/lib/rpm/brp-strip-static-archive %{__strip} /usr/lib/rpm/brp-strip-comment-note %{__strip} %{__objdump} %{nil}

######
# Red Hat-specific TeX configuration patches
######

# and sane defaults to build against can be inserted via sed
Patch5:		texlive-2007-browser.patch
Patch9:		texlive-teckit.patch

Patch21:	texlive-more_paths.patch
Patch22:	texlive-fedora_paths.patch

######
# TeX patches
######

Patch11:	texlive-2007-makej.patch
Patch12:	texlive-2007-badscript.patch
Patch17:	texlive-2007-tmpcleanup.patch
Patch18:	texlive-fmtutil-infloop.patch
Patch19:	texlive-2007-kpse-extensions.patch
Patch20:	texlive-CVE-2007-4033.patch
Patch25:	texlive-dvipsoverflow.patch
Patch26:	texlive-dviljktemp.patch
Patch27:	texlive-poppler.patch
Patch28:	texlive-man-notetex.patch
Patch29:	texlive-man-context.patch
Patch30:	texlive-lacheck.patch
Patch31:	texlive-elif.patch
Patch32:	texlive-getline.patch
Patch33:	texlive-poolfix.patch
Patch34:	texlive-dvipsconfig.patch
Patch35:	texlive-CVE-2010-0739,1440-integer-overflows.patch
Patch36:	texlive-execshield.patch

######
# mpeters contributed patches
######
# fixes man pages to utf-8
Patch42:	texlive-2007-copyright-utf8-man.patch
# use proper shellbang
Patch43:	texlive-2007-epstopdf-shellbang.patch

######
# Debian patches
######
Patch100:	texlive-Build_script.patch
Patch101:	texlive-mktexlsr_fixes.patch
Patch102:	texlive-fix_pkfix_invocation.patch
Patch104:	texlive-12a_fix_thumbpdf_invocation.patch
Patch105:	texlive-12b_fix_a2ping_invocation.patch
Patch106:	texlive-12c_fix_pdfcrop_invocation.patch
Patch107:	texlive-12d_fix_ebong_invocation.patch
Patch108:	texlive-12e_fix_vpe_invocation.patch
Patch109:	texlive-texdoc.patch
Patch114:	texlive-dvips_fontbug_fix_upstream.patch
Patch115:	texlive-maketexmf.patch
Patch117:	texlive-fmtutil_keep_failedlog.patch
Patch119:	texlive-checklib_fixes.patch
Patch123:	texlive-fix_makempx_installation.patch

######
# Mandriva patches
######
Patch202:	texlive-pdftex.patch

######
# Suse patches
######
Patch300:	texlive-source-icu.patch
Patch301:	texlive-source-t1lib.patch
Patch302:	texlive-source-warns.patch
Patch303:	texlive-source-x11r7.patch
Patch306:	texlive-source-CVE-2007-0650.patch

# 1000-: Japanese pTeX
Patch1000:	dvipsk-jpatch-pdvips.patch
Patch1004:	texlive-2007-jp-platex209.patch
Patch1005:	texlive-2007-pdvips.patch
Patch1006:	texlive-2007-ptex-3.1.10.patch
Patch1007:	texlive-2007-fmtutil-ptex.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	flex bison ed xdg-utils
BuildRequires:	desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires:	ncurses-devel zlib-devel libpng-devel gd-devel t1lib-devel
BuildRequires:	libSM-devel libICE-devel
# for non-modular xorg - use xorg-devel instead of above
BuildRequires:	Xaw3d-devel
BuildRequires:	poppler-devel >= 0.6.2-2
BuildRequires:	teckit-devel
Requires:	texlive-texmf = %{version}
Requires:	texlive-texmf-fonts = %{version}
Requires:	texlive-texmf-errata = %{version}
# make sure fonts package installed before running post - since
# fmtutil-sys is symlink to fmtutil
Requires(post):	%{_bindir}/fmtutil
Provides:	tex(tex)
Obsoletes:	tetex < 3.0-99
Provides:	tetex = 3.0-99
Obsoletes:	tetex-fonts < 3.0-99
Provides:	tetex-fonts = 3.0-99
Obsoletes:	texlive-fonts < 2007-6
Provides:	texlive-fonts = %{version}-%{release}

%description
TeXLive is an implementation of TeX for Linux or UNIX systems. TeX takes
a text file and a set of formatting commands as input and creates a
printable file as output. Usually, TeX is used in conjunction with
a higher level formatting package like LaTeX or PlainTeX, since TeX by
itself is not very user-friendly.

Install texlive if you want to use the TeX text formatting system. Consider
to install texlive-latex (a higher level formatting package which provides
an easier-to-use interface for TeX).

The TeX documentation is located in the texlive-doc package.

%package afm
Summary: A converter for PostScript(TM) font metric files, for use with TeX
Group: Applications/Publishing
Obsoletes: tetex-afm < 3.0-99
Provides:  tetex-afm = 3.0-99
Requires: texlive-texmf-afm = %{version}
Requires: texlive-texmf-errata = %{version}

%description afm
texlive-afm provides afm2tfm, a converter for PostScript(TM) font metric
files. PostScript fonts are accompanied by .afm font metric files
which describe the characteristics of each font. To use PostScript
fonts with TeX, TeX needs .tfm files that contain similar information.
Afm2tfm will convert .afm files to .tfm files.

If you are installing texlive in order to use the TeX text formatting
system and PostScript files, you will need to install texlive-afm. You will
also need to install texlive-dvips (for converting .dvi files to PostScript
format for printing on PostScript printers), texlive-latex (a higher level
formatting package which provides an easier-to-use interface for TeX), and
xdvi (for previewing .dvi files in X).

The TeX documentation is located in the texlive-doc package.

%package utils
Summary: TeXLive utilities using ghostscript and metafont with X support
Group: Applications/Publishing
Requires: texlive = %{version}-%{release}
Requires: texlive-dvips = %{version}-%{release}
Requires: ghostscript

%description utils
This package contains TeXLive utilities using ghostscript and metafont
with X support.

%package xetex
Summary: TeX typesetting engine using Unicode with OpenType or AAT support
Group: Applications/Publishing
Requires: texlive = %{version}-%{release}
Requires: texlive-texmf-xetex = %{version}
Requires: dvipdfmx xdvipdfmx
Provides: tex(xetex)

%description xetex
XeTeX is a TeX typesetting engine using Unicode and supporting modern
font technologies such as OpenType or AAT. Initially developed for Mac
OS X only, it is now available for all major platforms. It natively
supports Unicode and the input file is assumed to be in UTF-8 encoding
by default.

%package dvips
Summary: A DVI to PostScript converter for the TeX text formatting system
Group: Applications/Publishing
Requires: texlive = %{version}-%{release}
Obsoletes: tetex < 3.0-99
Obsoletes: tetex-dvips < 3.0-99
Provides:  tetex-dvips = 3.0-99
Requires: texlive-texmf-dvips = %{version}
Requires: texlive-texmf-errata = %{version}
Provides: tex(dvips)
Requires: psutils

%description dvips
Dvips converts .dvi files, for example those produced by the TeX text
formatting system, to PostScript(TM) format.

If you are installing texlive, so that you can use the TeX text
formatting system without direct PDF compilation, consider to install
texlive-dvips. In addition, you will need to install texlive-latex
(a higher level formatting package which provides an easier-to-use
interface for TeX), and xdvi (for previewing .dvi files in X).

%package dviutils
Summary: A collection of utilities for working with dvi files
Group: Applications/Publishing
# not positive about this requires, pretty sure though
Requires: texlive = %{version}-%{release}
# used to be in tetex, but has a separate upstream
Requires: dvipng dvipdfm
# some dvi utilities used to be in tetex
Obsoletes: tetex < 3.0-99

%description dviutils
The texlive-dviutils package includes a set of tools for working with dvi
files. You only need this package if you plan to manipulate existing dvi files.

%package latex
Summary: The LaTeX front end for the TeX text formatting system
Group: Applications/Publishing
Requires: texlive = %{version}-%{release}, texlive-dvips = %{version}-%{release}
Requires: netpbm-progs
# make sure main and fonts package installed before running post
Requires(post): %{_bindir}/fmtutil %{_bindir}/fmtutil-sys
Requires(post): %{_bindir}/texconfig-sys /sbin/install-info
BuildRequires: ghostscript netpbm-progs
Obsoletes: tetex < 3.0-99
Obsoletes: tetex-latex < 3.0-99
Provides:  tetex-latex = 3.0-99
Requires: texlive-texmf-latex = %{version}
Requires: texlive-texmf-errata = %{version}
Requires: texlive-utils = %{version}-%{release}
Provides: tex(latex)

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to
use than TeX. LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users. It also allows to
compile LaTeX files directly to PDF format.

The TeX documentation is located in the texlive-doc package.

%package east-asian
Summary: Support for East Asian languages in TeXLive
Group: Applications/Publishing
Requires: texlive = %{version}-%{release}
Requires: texlive-latex = %{version}-%{release}
Requires: texlive-texmf-dvips = %{version}
Requires: texlive-texmf-east-asian = %{version}
Requires: texlive-texmf-errata-east-asian = %{version}
Requires: mendexk
Obsoletes: texlive-japanese < 2007-20
Provides: texlive-japanese = %{version}-%{release}
Provides: tex(japanese)
Provides: tex(east-asian)

%description east-asian
East Asian support for TeXLive.

%package context
Summary: ConTeXt is a document preparation system based on TeX
Group: Applications/Publishing
Requires: texlive = %{version}-%{release}
Requires: texlive-texmf-context = %{version}
Requires: texlive-texmf-errata-context = %{version}
Requires: ruby
Provides: tex(context)

%description context
ConTeXt is a document preparation system based on TeX.

%package -n kpathsea
Summary: Path searching library for TeX-related files
Group:   Development/Libraries
Obsoletes: tetex-fonts < 3.0-99

%description -n kpathsea
The library is at the centre of pretty much all Unix-based TeX
executable. It is no longer distributed separately, but rather
consititutes a central part of the sources of the TeX-live
distribution.

%package -n kpathsea-devel
Summary: Files needed to build software against kpathsea
Group:   Development/Libraries
Requires: kpathsea = %{version}

%description -n kpathsea-devel
This package includes the kpathsea header files and the libkpathsea.so
symbolic link.

You only need to install this package if you will be compiling software that
wants to link against the kpathsea library.

%package -n mendexk
Summary: Replacement for makeindex with many enhancements
Group: Applications/Publishing
Version: %{mendexk_ver}
#Url: ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/mendex/
#Source0: ftp://ftp.ascii.co.jp/pub/TeX/ascii-ptex/mendex/mendexk%{version}.tar.bz2

%description -n mendexk
Replacement for makeindex with many enhancements.

# without this define, the version is overriden by separated subpackages
# versions
%define version %{texlive_ver}

%prep
%setup -q -T -c -a0

# fix for debuginfo rpmlint happiness
chmod -x texk/dvipdfm/macglyphs.h
chmod -x texk/dvipdfm/ttf.c
chmod -x texk/dvipdfm/encodings.c

######
# Red Hat-specific TeX configuration patches
######
# Use htmlview first
%patch5 -p1 -b .browser
%patch9 -p1 -b .teckit
%patch22 -p1 -b .fedora_paths

######
# TeX patches
######

# Fix parallel builds.
%patch11 -p1 -b .makej
# Don't use PID for temporary file names in scripts (RH bug #41269)
%patch12 -p1 -b .badscript
# Always cleanup temporary directories for texconfig, updmap, fmtutil
#  (RH #172534)
%patch17 -p1 -b .tmpcleanup
# fmtutil won't hang in infinite loop (#437008)
%patch18 -p1 -b .infloop
%patch19 -p0 -b .kpse-extensions
%patch20 -p1 -b .CVE-2007-4033
%patch21 -p1 -b .more_paths
%patch25 -p1 -b .dvipsoverflow
%patch26 -p1 -b .dviljktemp
%patch27 -p1 -b .poppler
%patch28 -p1 -b .notetex
%patch29 -p1 -b .man-context
%patch30 -p1 -b .lacheck
%patch31 -p1 -b .elif
%patch32 -p1 -b .getline
%patch33 -p1 -b .poolfix
%patch34 -p1 -b .dvipsconfig
%patch35 -p1 -b .CVE-2010-0739,1440
%patch36 -p1 -b .execshield

# fix non utf man pages
%patch42 -p1 -b .notutf8-2
# user a proper shellbang
%patch43 -p1 -b .perl

%patch100 -p3
%patch101 -p1 -b .mktexlsr_fixes
%patch102 -p3
%patch104 -p3
%patch105 -p3
%patch106 -p3
%patch107 -p3
%patch108 -p3
%patch109 -p1
%patch114 -p3
%patch115 -p3
%patch117 -p3
%patch119 -p3
%patch123 -p3

%patch202 -p1 -b .pdftex

%patch300 -p0
%patch301 -p1
%patch302 -p0
%patch303 -p0
%patch306 -p0

%patch1007 -p1 -b .ptex

%if %{disable_lcdf_typetools}
pushd utils
rm -rf lcdf-typetools
popd
%endif

## Japanese pTeX
# set platex to Japanese pLaTeX. original one is moved to platex-pl
sed -e s/^platex/platex-pl/g \
    -e s/^pdfplatex/pdfplatex-pl/g \
    -e s/platex\.ini/platex\-pl\.ini/g \
     -i texk/web2c/fmtutil.in

# Prepare pTeX
tar xfz %{SOURCE1000} -C texk/web2c/
cd texk/web2c/ptex-src-%{ptex_src_ver}
sed -i -e  's|/{ptex/{platex,generic,},tex/{latex,generic,}}|/{ptex/platex,{p,}tex/latex,{p,}tex/generic,{p,}tex}|g' -e 's/| uniq//g' mkconf
%patch1004 -p1 -b .fmts
%patch1006 -p1
cd -

# Prepare Japanese dvips
mkdir pdvipsk
tar xfz %{SOURCE1001} -C pdvipsk
cp -lR texk/dvipsk texk/pdvipsk
cd pdvipsk
%patch1005 -p0
cd -
patch -d texk/pdvipsk -p1 < pdvipsk/dvipsk-%{pdvipsk_ver}.patch || :
%patch1000 -p1 -b .pdvips
ln -s dvips.1 texk/pdvipsk/pdvips.1

# set up mendexk
tar xfz %{SOURCE1002} -C texk

%build
set -x
# define CCACHE_DIR to let the build pass with ccache enabled.
export CCACHE_DIR=$HOME/.ccache
unset TEXINPUTS ||:
unset HOME ||:

%{__rm} -r libs/{teckit,obsdcompat}

# Japanese pTeX
pushd texk
$RPM_BUILD_DIR/%{name}-%{version}/texk/autoconf2.13 -m $RPM_BUILD_DIR/%{name}-%{version}/texk/etc/autoconf
popd

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%configure \
%if %{default_letter_paper}
        --disable-a4 \
%endif
	--enable-shared=yes \
	--with-system-ncurses \
	--with-system-zlib \
	--with-system-pnglib \
	--with-system-gd \
	--without-system-icu \
	--with-icu-include=%{_includedir}/unicode \
	--with-system-freetype \
	--with-freetype-include=%{_includedir}/freetype \
	--with-system-freetype2 \
	--with-freetype2-include=%{_includedir}/freetype2 \
	--with-system-t1lib \
	--without-texlive \
	--without-t1utils \
	--without-psutils \
	--without-ps2eps \
	--without-pdfopen \
	--without-ttf2pk \
	--disable-multiplatform \
	--without-dialog --without-texinfo --without-texi2html \
	--without-tex4htk \
	--without-detex --without-dvi2tty \
%if %{disable_lcdf_typetools}
	--with-lcdf-typetools=no \
%endif
	--without-xdvik \
	--with-mf-x-toolkit=yes \
	--without-cxx-runtime-hack \
	--without-dvipng \
	--without-dvipdfm \
	--without-dvipdfmx \
	--without-xdvipdfmx

# Remove everything except:
# icu: includes some changes
# md5: the aladdin md5 code (not a library)
%{__rm} -r libs/{curl,expat,freetype,freetype2,gd,howto,jpeg,libgnuw32,libgsw32,libpng,libttf,ncurses,regex,unzip,zlib,type1,t1lib,xpdf}/

# parallel build fails in libs/icu-xetex/common, build this one sequentially
cd libs/icu-xetex
make
cd -

# compile the rest parallelly
make %{?_smp_mflags}

cd texk/web2c/ptex-src-%{ptex_src_ver}
./configure EUC
make
cd -

# mendexk build
cd texk/mendexk%{mendexk_ver}
./configure EUC
make
cd -


%install
rm -rf %{buildroot}
export CCACHE_DIR=$HOME/.ccache
unset TEXINPUTS || :
unset HOME || :

mkdir -p %{buildroot}%{_texmf_main}
mkdir -p %{buildroot}%{_texmf_var}/web2c
mkdir -p %{buildroot}%{_texmf_conf}

export LD_LIBRARY_PATH=`pwd`/texk/kpathsea/.libs

# a temporary placeholder for texmf.cnf
mkdir -p %{buildroot}%{_datadir}/texmf-local/web2c
cp -a texk/kpathsea/texmf.cnf %{buildroot}%{_datadir}/texmf-local/web2c

%makeinstall \
        texmf=%{buildroot}%{_texmf_main} \
        texmfmain=%{buildroot}%{_texmf_main}

rm -rf %{buildroot}%{_datadir}/texmf-local/

# remove all .la files
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} | grep -e "\\.la$" | xargs rm -f

# set executable bit for the library for debuginfo creation
chmod a+x %{buildroot}%{_libdir}/libkpathsea.so.*.*

## remove what is packages in other Fedora packages
# jadetex
rm -f %{buildroot}%{_bindir}/jadetex
rm -f %{buildroot}%{_bindir}/pdfjadetex
# xmltex
rm -f %{buildroot}%{_bindir}/xmltex
rm -f %{buildroot}%{_bindir}/pdfxmltex
# octave-forge
### looks to me like a name clash ?? Octave mex looks like it has nada to
### to with TeX
rm -f %{buildroot}%{_bindir}/mex
### not in octave-forge, nuking anyway
rm -f %{buildroot}%{_bindir}/pdfmex
rm -f %{buildroot}%{_bindir}/utf8mex

# these are owned by texmf-fonts package
rm -f %{buildroot}%{_texmf_main}/ls-R

# keep fmtutil.cnf used for the initial configuration in doc
rm -rf __fedora_kpathsea
mkdir -p __fedora_kpathsea/
mv %{buildroot}%{_texmf_main}/web2c/fmtutil.cnf __fedora_kpathsea/fmtutil.cnf-init
cp %{SOURCE1} __fedora_kpathsea/

# this file is different from the one in texmf-fonts, since it is
# the one from kpathsea which isn't specific of texlive. It is only
# used during build and to set the kpathsea default paths, however.
# Kept as documentation together with paths.h since they describe
# what the kpathsea default paths are
mkdir -p __fedora_kpathsea/kpathsea_defaults
mv %{buildroot}%{_texmf_main}/web2c/texmf.cnf __fedora_kpathsea/kpathsea_defaults/texmf-kpathsea-defaults.cnf
cp texk/kpathsea/paths.h __fedora_kpathsea/kpathsea_defaults

# these are owned by texmf-doc package
rm -rf %{buildroot}%{_texmf_main}/doc/tetex

# remove pool files, they belong to texlive-texmf
rm -rf %{buildroot}%{_texmf_main}/web2c/*.pool
# ptex pool file is added later, and therefore kept

# Japanese pTeX
rm -f %{buildroot}%{_bindir}/platex
# Convert documents to UTF-8
mkdir -p %{buildroot}%{_texmf_main}/doc/ptex/ptex-src-%{name} \
         %{buildroot}%{_texmf_main}/doc/pdvipsk
cd texk/web2c/ptex-src-%{ptex_src_ver}
iconv -f ISO-2022-JP -t UTF-8 \
      COPYRIGHT.jis \
      -o %{buildroot}%{_texmf_main}/doc/ptex/ptex-src-%{name}/COPYRIGHT-ja
for i in README.txt Changes.txt ; do
  iconv -f EUC-JP -t UTF-8 ${i} \
        -o %{buildroot}%{_texmf_main}/doc/ptex/ptex-src-%{name}/${i}
done
cd -
cd pdvipsk
for i in ChangeLog.jpatch README.jpatch ; do
  iconv -f EUC-JP -t UTF-8 ${i} -o %{buildroot}%{_texmf_main}/doc/pdvipsk/${i}
done
cd -

cd texk/web2c/ptex-src-%{ptex_src_ver}
%makeinstall INSTALL="install -p" prefix=%{buildroot}%{_prefix} \
        texmf=%{buildroot}%{_texmf_main} \
        texmfmain=%{buildroot}%{_texmf_main}
# texmf.cnf is prepared by texlive-texmf package.
rm %{buildroot}%{_texmf_main}/web2c/texmf.cnf
cd -

# mendexk install
cd texk/mendexk%{mendexk_ver}

sh ../libtool --mode=install install mendex %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/ja/man1
iconv -f EUC-JP -t UTF-8 mendex.1 -o %{buildroot}%{_mandir}/ja/man1/mendex.1
mkdir -p %{buildroot}%{_datadir}/texmf/doc/mendexk-%{name}
install -p -m 644 COPYRIGHT ChangeLog %{buildroot}%{_datadir}/texmf/doc/mendexk-%{name}
iconv -f EUC-JP -t UTF-8 README -o %{buildroot}%{_datadir}/texmf/doc/mendexk-%{name}/README
iconv -f ISO-2022-JP -t UTF-8 COPYRIGHT.jis -o %{buildroot}%{_datadir}/texmf/doc/mendexk-%{name}/COPYRIGHT.jis
cd -

# remove useless files in texconfig
rm -rf %{buildroot}%{_texmf_main}/texconfig/{g,v,x,README,generic}

# move the configuration files that should be under user control
mkdir -p %{buildroot}%{_texmf_conf}/{web2c/,dvipdfm/}
mv %{buildroot}%{_texmf_main}/web2c/mktexdir.opt %{buildroot}%{_texmf_conf}/web2c/

# separated projects
rm %{buildroot}%{_bindir}/devnag
rm %{buildroot}%{_bindir}/afm2pl %{buildroot}%{_mandir}/man1/afm2pl.1*

# remove unused ConTeXt stuff
rm %{buildroot}%{_mandir}/man1/texfind.1* %{buildroot}%{_mandir}/man1/fdf2tex.1*

# remove (x)dvipdfmx related stuff
rm -f %{buildroot}%{_bindir}/dvipdfmx
rm -f %{buildroot}%{_bindir}/xdvipdfmx
rm -rf %{buildroot}%{_texmf_main}/dvipdfm

# remove tcfmgr stuff, it is packaged in texlive-texmf (#442135)
rm -rf %{buildroot}%{_texmf_main}/texconfig/tcfmgr*

# remove texdoc and texdoctk when texlive-doc subpackage creation is not requested
rm -f \
%{buildroot}%{_bindir}/texdoc \
%{buildroot}%{_bindir}/texdoctk \
%{buildroot}%{_mandir}/man1/texdoc.1* \
%{buildroot}%{_mandir}/man1/texdoctk.1*

%clean
rm -rf %{buildroot}

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/web2c.info.gz %{_infodir}/dir
[ -x %{_bindir}/fmtutil-sys ] && %{_bindir}/fmtutil-sys --all &> /dev/null
[ -x %{_bindir}/updmap-sys ] && %{_bindir}/updmap-sys --syncwithtrees &> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post afm
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post context
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post dvips
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/dvips.info.gz %{_infodir}/dir
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post dviutils
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post east-asian
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post latex
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/latex.info.gz %{_infodir}/dir
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys init &> /dev/null
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
[ -x %{_bindir}/fmtutil-sys ] && %{_bindir}/fmtutil-sys --all &> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post xetex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%post -n kpathsea
[ -x /sbin/ldconfig ] && /sbin/ldconfig
[ -x /sbin/install-info ] && /sbin/install-info %{_infodir}/kpathsea.info.gz %{_infodir}/dir
:


%preun
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/web2c.info.gz %{_infodir}/dir
fi
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%preun dvips
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/dvips.info.gz %{_infodir}/dir
fi
:

%preun latex
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/latex.info.gz %{_infodir}/dir
fi
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%preun -n kpathsea
[ -x /sbin/ldconfig ] && /sbin/ldconfig
if [ "$1" = 0 ]; then
  [ -x /sbin/install-info ] && /sbin/install-info --delete %{_infodir}/kpathsea.info.gz %{_infodir}/dir
fi
:

%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun afm
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun context
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun east-asian
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun dviutils
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun dvips
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun latex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun xetex
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon -R %{_texmf_var}/
fi
:

%postun -n kpathsea
[ -x /sbin/ldconfig ] && /sbin/ldconfig
:

%files
%defattr(-,root,root,-)
# config files
%dir %{_texmf_conf}
%dir %{_texmf_conf}/web2c/
%dir %{_texmf_main}/web2c/
%dir %{_texmf_main}/doc/
%doc %{_texmf_main}/doc/bibtex8/
%doc __fedora_kpathsea/fmtutil.cnf-init
%config(noreplace) %{_texmf_conf}/web2c/mktexdir.opt
# binaries
%{_bindir}/aleph
%{_bindir}/amstex
%{_bindir}/bibtex
%{_bindir}/ctangle
%{_bindir}/ctie
%{_bindir}/cweave
%{_bindir}/dmp
%{_bindir}/dvitomp
%{_bindir}/etex
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/fontinst
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/kpseaccess
%{_bindir}/kpsepath
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsetool
%{_bindir}/kpsewhich
%{_bindir}/kpsexpand
%{_bindir}/kpsewhere
%{_bindir}/lambda
%{_bindir}/lamed
%{_bindir}/mag
%{_bindir}/makeindex
%{_bindir}/makempx
%{_bindir}/mft
%{_bindir}/mkindex
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mktexfmt
%{_bindir}/mktexlsr
%{_bindir}/mktexmf
%{_bindir}/mktextfm
%{_bindir}/mpost
%{_bindir}/mpto
%{_bindir}/newer
%{_bindir}/ofm2opl
%{_bindir}/omega
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf
%{_bindir}/patgen
%{_bindir}/pdfetex
%{_bindir}/pdftex
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/pktogf
%{_bindir}/pktype
%{_bindir}/pltotf
%{_bindir}/pooltype
%{_bindir}/ps2frag
%{_bindir}/ps2pk
%{_bindir}/rubibtex
%{_bindir}/rumakeindex
%{_bindir}/tangle
%{_bindir}/tex
%{_bindir}/texconfig
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texhash
%{_bindir}/texlinks
%{_bindir}/tftopl
%{_bindir}/tie
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_bindir}/vftovp
%{_bindir}/vptovf
%{_bindir}/weave
# new files not in Fedora tetex
%{_bindir}/bibtex8
%{_bindir}/csplain
# separated project
%{_bindir}/mltex
%{_bindir}/pdfcsplain
# separated project
%{_bindir}/eplain
%{_bindir}/extconv
%{_bindir}/musixflx
%{_bindir}/physe
%{_bindir}/phyzzx
%{_bindir}/texsis
# other utilities
%{_bindir}/pdftosrc
# man pages
%{_mandir}/man1/amstex.1*
%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/ctie.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{_mandir}/man1/newer.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*
%{_mandir}/man1/patgen.1*
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/pooltype.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/ps2pk.1*
%{_mandir}/man1/rubibtex.1*
%{_mandir}/man1/rumakeindex.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texconfig-sys.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/updmap.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
%{_mandir}/man5/fmtutil.cnf.5*
# new files not in Fedora tetex
%{_mandir}/man5/updmap.cfg.*
# man pages for other utilities
%{_mandir}/man1/pdftosrc.1*
# other stuff
%{_infodir}/web2c.info.*
%{_texmf_main}/web2c/*.opt
%{_texmf_main}/web2c/mktexdir
%{_texmf_main}/web2c/mktexnam
%{_texmf_main}/web2c/mktexupd
%{_texmf_main}/bibtex/

%files utils
%defattr(-,root,root,-)
%{_bindir}/a2ping
%{_bindir}/e2pall
%{_bindir}/epstopdf
%{_bindir}/gsftopk
%{_bindir}/mf
%{_bindir}/mf-nowin
%{_bindir}/mktexpk
%{_bindir}/pdfcrop
%{_bindir}/ps4pdf
%{_bindir}/thumbpdf
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/thumbpdf.1*

%files xetex
%defattr(-,root,root,-)
%{_bindir}/xetex
%{_bindir}/xelatex

%files afm
%defattr(-,root,root,-)
%{_bindir}/afm2tfm
%{_bindir}/ttf2afm
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/ttf2afm.1*

%files dvips
%defattr(-,root,root,-)
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvips
%{_bindir}/dvired
%{_bindir}/odvips
%{_texmf_main}/dvips/
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/odvips.1*
%{_infodir}/dvips.info.*

%files dviutils
%defattr(-,root,root,-)
%{_bindir}/dt2dv
%{_bindir}/dv2dt
%{_bindir}/dvicopy
%{_bindir}/dvihp
%{_bindir}/dvitype
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dvidvi
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6
%{_bindir}/dvipos
%{_bindir}/dviselect
%{_bindir}/dvitodvi
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dvidvi.1*
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*
%{_mandir}/man1/dvipos.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvitype.1*

%files latex
%defattr(-,root,root,-)
%{_bindir}/latex
%{_bindir}/pdflatex
%{_bindir}/pslatex
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pdflatex.1*
%{_mandir}/man1/pslatex.1*
%{_infodir}/latex.info.*
# not in fedora tetex
%{_bindir}/cslatex
%{_bindir}/lacheck
%{_bindir}/mllatex
%{_bindir}/pdfcslatex
%{_mandir}/man1/lacheck.1*

%files -n kpathsea
%defattr(-,root,root,-)
%doc __fedora_kpathsea/kpathsea_defaults/ __fedora_kpathsea/lgpl.txt
%{_libdir}/libkpathsea.so.*
%{_infodir}/kpathsea.info.*

%files -n kpathsea-devel
%defattr(-,root,root,-)
%{_includedir}/kpathsea/
%{_libdir}/libkpathsea.so
# yes - packaging the static too. Some programs apparently can't link
#  against the shared. I can't name any, but so i hear.
%{_libdir}/libkpathsea.a

%files -n mendexk
%defattr(-,root,root,-)
%doc %{_texmf_main}/doc/mendexk-%{name}/
%{_bindir}/mendex
%{_mandir}/ja/man1/mendex.1*

%files east-asian
%defattr(-,root,root,-)
%doc %{_texmf_main}/doc/pdvipsk/
%doc %{_texmf_main}/doc/ptex/
%{_texmf_main}/fonts/map/pdvips/
%{_texmf_main}/pdvips/
%{_texmf_main}/web2c/ptex.pool
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/bg5conv
%{_bindir}/cef5conv
%{_bindir}/cefconv
%{_bindir}/cefsconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/hbf2gf
%{_bindir}/jbibtex
%{_bindir}/pdfplatex-pl
%{_bindir}/pdvips
%{_bindir}/pdvitype
%{_bindir}/platex
%{_bindir}/platex-pl
%{_bindir}/platex209
%{_bindir}/ptex
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex
%{_bindir}/opdvips
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/pdvips.1*
%{_mandir}/man1/opdvips.1*

%files context
%defattr(-,root,root,-)
%{_bindir}/ctxtools
%{_bindir}/exatools
%{_bindir}/luatools
%{_bindir}/makempy
%{_bindir}/mpstools
%{_bindir}/mptopdf
%{_bindir}/mtxtools
%{_bindir}/pdftools
%{_bindir}/pstopdf
%{_bindir}/rlxtools
%{_bindir}/runtools
%{_bindir}/texexec
%{_bindir}/texfont
%{_bindir}/texmfstart
%{_bindir}/textools
%{_bindir}/texutil
%{_bindir}/tmftools
%{_bindir}/xmltools
%{_mandir}/man1/ctxtools.1*
%{_mandir}/man1/makempy.1*
%{_mandir}/man1/mptopdf.1*
%{_mandir}/man1/pdftools.1*
%{_mandir}/man1/pstopdf.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texfont.1*
%{_mandir}/man1/texmfstart.1*
%{_mandir}/man1/textools.1*
%{_mandir}/man1/texutil.1*

%changelog
* Thu Jun 24 2010 Jindrich Novy <jnovy@redhat.com> 2007-56
- add LGPL license to kpathsea's docs (#607142)

* Tue Jun 01 2010 Jindrich Novy <jnovy@redhat.com> 2007-55
- add -fno-strict-aliasing (#596214)

* Mon May 24 2010 Jindrich Novy <jnovy@redhat.com> 2007-54
- clear executable stack flag in xetex binary (#572891)

* Tue May 11 2010 Jindrich Novy <jnovy@redhat.com> 2007-53
- fix cross-package symlink, move mf-nowin to texlive-utils (#584289)

* Mon May 10 2010 Jindrich Novy <jnovy@redhat.com> 2007-52
- add complete fix for CVE-2010-0739 and CVE-2010-1440

* Wed Apr 22 2010 Jindrich Novy <jnovy@redhat.com> 2007-51
- fix integer overflow - CVE-2010-0739

* Wed Apr 21 2010 Jindrich Novy <jnovy@redhat.com> 2007-50
- do not restore contexts in kpathsea for unowned directory (#579219)

* Thu Mar 04 2010 Jindrich Novy <jnovy@redhat.com> 2007-49
- remove texlive-doc subpackage (#568785)

* Tue Jan 12 2010 Jindrich Novy <jnovy@redhat.com> 2007-48
- add missing defattr to filelists
- do not own /var/lib/texmf/web2c/, it is owned by texlive-texmf
- use official tarball for dvipsk-jpatch

* Mon Nov 02 2009 Jindrich Novy <jnovy@redhat.com> 2007-47
- fix post/postun scriptlets (#532466)

* Fri Oct 23 2009 Jindrich Novy <jnovy@redhat.com> 2007-46
- add missing dependency on kpathsea

* Thu Oct 15 2009 Jindrich Novy <jnovy@redhat.com> 2007-45
- make kpathsea not dependent on texlive
- fix lacheck again (#451513)
- fix dvips configuration (#467542)
- update kpathsea description and summary (#519257)
- use upstream patch to fix pool overflow CVE-2009-1284 (#492136)
- don't complain if the pdvipsk hunks touching config.ps don't apply

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Jindrich Novy <jnovy@redhat.com> - 2007-43
- fix pdftoepdf and rebuild because of poppler soname bump (#501651)

* Thu Apr 02 2009 Jindrich Novy <jnovy@redhat.com> - 2007-42
- avoid clashes with getline() from glibc
- increase default bibtex/jbibtex limits (#492136)

* Thu Feb 26 2009 Jindrich Novy <jnovy@redhat.com> - 2007-41
- texlive-east-asian now requires texlive-texmf-east-asian (#487258)
- do not attempt to remove old fonts via cron in /var/lib/texmf,
  fonts are stored in ~/.texlive2007/texmf-var per-user
  (#477833, #463975, #453468)
- use correct paths in brp-* post install scriptlets (#468179)
- fix build with gcc4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Matthias Clasen <mclasen@redhat.com> - 2007-39
- Rebuild against new poppler
- Update poppler patch to remove references to xpdfVersion

* Wed Aug 27 2008 Jindrich Novy <jnovy@redhat.com> - 2007-35
- texlive-context requires texlive-texmf-context (#455163)
- fix lacheck to not to segfault (#451513)
- rediff some patchesto be applicable with zero fuzz

* Mon Jun 23 2008 Jindrich Novy <jnovy@redhat.com> - 2007-34
- do not directly depend on restorecon and run it only if
  selinux is enabled

* Thu Jun 19 2008 Jindrich Novy <jnovy@redhat.com> - 2007-33
- platex belongs to texlive-east-asian otherwise it is a dangling
  symlink in texlive-latex

* Wed Jun 18 2008 Jindrich Novy <jnovy@redhat.com> - 2007-32
- texlive-xetex now provides tex(xetex) (#451774)
- attempt to fix lacheck segfault (#451513)
- avoid multiple ownership of texconfig stuff (#442135)

* Mon May 12 2008 Jindrich Novy <jnovy@redhat.com> - 2007-31
- don't build/package dvipdfm, it's now packaged separately (#445983),
  thanks to Jonathan Underwood
- remove F8 related chunks from spec

* Mon May 05 2008 Jindrich Novy <jnovy@redhat.com> - 2007-30
- fix SELinux contexts everywhere possible, don't allow restorecon
  to fail (#444922)
- add missing post/postun scriptlets for subpackages

* Mon Apr 21 2008 Jindrich Novy <jnovy@redhat.com> - 2007-29
- run restorecon on /var/lib/texmf to avoid access denials
  if SELinux is in enforcing mode (#443286, #442161)

* Tue Mar 18 2008 Jindrich Novy <jnovy@redhat.com> - 2007-28
- xelatex requires xdvipdfmx

* Fri Mar 14 2008 Jindrich Novy <jnovy@redhat.com> - 2007-27
- remove dvipdfmx completely, also for F8 (related #437448)
- kpathsea requires texlive again (#437458)

* Thu Mar 13 2008 Jindrich Novy <jnovy@redhat.com> - 2007-26
- rebuild against the new poppler 0.7.2 (poppler's soname was bumped)

* Wed Mar 12 2008 Jindrich Novy <jnovy@redhat.com> - 2007-25
- fix fmtutil to not to hang in infinite loop, thanks to
  Stepan Kasal (#437008)
- fix search paths in texmf.cnf, thanks to Patrice Dumas (#436949)

* Sat Mar 08 2008 Jindrich Novy <jnovy@redhat.com> - 2007-24
- put back dvipdfmx requires for xelatex (#433225)
- don't compile unpackaged stuff
- enable parallel build

* Tue Mar 04 2008 Jindrich Novy <jnovy@redhat.com> - 2007-23
- move MetaPost back to the main package from texlive-context
- don't package dvipdfmx, it is now packaged separately (#433225)

* Mon Mar 03 2008 Jindrich Novy <jnovy@redhat.com> - 2007-22
- specify required version more properly for subpackages
- move xelatex to texlive-xetex

* Sat Mar 01 2008 Jindrich Novy <jnovy@redhat.com> - 2007-21
- require texlive-utils in texlive-latex

* Thu Feb 28 2008 Jindrich Novy <jnovy@redhat.com> - 2007-20
- move mktexpk to texlive-utils (#435176)
- rename texlive-japanese to texlive-east-asian
- move ghostscript Requires to dvipdfmx
- remove trailing spaces from spec

* Thu Feb 21 2008 Jindrich Novy <jnovy@redhat.com> - 2007-19
- remove dvipng, it's now packaged separately (#431356)

* Tue Feb 19 2008 Jindrich Novy <jnovy@redhat.com> - 2007-18
- package ConTeXt separately to get rid of the ruby dependency
- fix summary for texlive-japanese
- remove man pages with no corresponding binaries

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2007-17
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Jindrich Novy <jnovy@redhat.com> - 2007-16
- package Japanese separately -> texlive-japanese
- add missing BR: texlive-texmf-fonts (#430338)
- temporarily disable BR: texlive in kpathsea

* Wed Jan 23 2008 Jindrich Novy <jnovy@redhat.com> - 2007-15
- dependency pruning: (#428489, #429753)
  - package XeTeX separately
  - move ghostscript utilities (a2ping, e2pall, epstopdf, gsftopk,
    pdfcrop, ps4pdf, thumbpdf) and metafont with X support
    to texlive-utils subpackage
  - move allcm, allec, allneeded to texlive-dvips
  - package xdvipdfmx in dvipdfmx subpackage
  - only texlive-doc now requires xdg-utils

* Tue Jan 22 2008 Jindrich Novy <jnovy@redhat.com> - 2007-14
- use xdg-open(1) in texdoctk (#429659)
- fix bad syntax of texmfstart man page

* Fri Jan 18 2008 Jindrich Novy <jnovy@redhat.com> - 2007-13
- don't copy original pdftex map files but regenerate them
  with the correct updmap.cfg file updated in texlive-texmf
  (Related: #425804)
- install mendex via libtool (#428507)

* Thu Jan 17 2008 Jindrich Novy <jnovy@redhat.com> - 2007-12
- remove all references to teTeX from the packaged man pages
  and update links to point correctly to upstream mailing
  list and web page
- drop xpdf patch, we link against poppler now

* Wed Jan 16 2008 Jindrich Novy <jnovy@redhat.com> - 2007-11
- temporary fix to pdflatex to not to warn verbosely because of
  ambiguous entries in pdflatex.map (#425804)
- update post scriptlets, spec cleanup

* Tue Jan 15 2008 Jindrich Novy <jnovy@redhat.com> - 2007-10
- don't build/package xdvik/pxdvik, it's now separated
- fix texlive-doc requires, description
- use virtual provides with parentheses to avoid clashes
  with real packages (#410401)

* Mon Jan 14 2008 Jindrich Novy <jnovy@redhat.com> - 2007-9
- unify texlive and texlive-fonts filelists
- package texdoc and texdoctk to a separate subpackage
  texlive-doc, because of the Perl-Tk dependencies and logic

* Mon Jan 07 2008 Jindrich Novy <jnovy@redhat.com> - 2007-8
- add tex-latex and tex-dvips virtual provides
- mktexlsr fixes from Patrice Dumas

* Fri Jan 04 2008 Jindrich Novy <jnovy@redhat.com> - 2007-7
- add tetex-fonts virtual provides to main texlive package (#427521)

* Wed Jan 02 2008 Jindrich Novy <jnovy@redhat.com> - 2007-6
- unify texlive and texlive-fonts packages and obsolete
  texlive-fonts (related: #426388)
- move subpackages versions to the top of spec file
- changes from Patruce Dumas:
  * remove BuildRequires on texmf packages
  * don't create .fmt files during the build
  * ship the ptex.pool file

* Mon Dec 17 2007 Jindrich Novy <jnovy@redhat.com> - 2007-5
- add tex virtual provide
- BuildRequire texlive-fonts for kpathsea (thanks to Patrice Dumas)

* Mon Dec 10 2007 Jindrich Novy <jnovy@redhat.com> - 2007-4
- update japanese, chinese, korean paths to fonts in vfontmap (#418081, #392221)
- create customized cid-x.map for dvipdfmx (#418091)

* Tue Dec 04 2007 Jindrich Novy <jnovy@redhat.com> - 2007-3
- try to obsolete tetex correctly

* Tue Dec 04 2007 Jindrich Novy <jnovy@redhat.com> - 2007-2
- avoid conflicts with tetex-doc package

* Sun Dec 02 2007 Jindrich Novy <jnovy@redhat.com> - 2007-1
- buildrequire texlive-texmf-fonts and texlive-texmf-latex for ptex
- drop BR gawk

* Fri Nov 30 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.17
- add .gz suffix to info pages so that they gets successfully
  removed in preun phase

* Thu Nov 29 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.16
- drop Requires: poppler
- require texlive-fonts in kpathsea
- replace htmlview by xdg-open

* Fri Nov 16 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.15
- fix t1lib flaw CVE-2007-4033 (#352271)
- fix CVE-2007-4352 CVE-2007-5392 CVE-2007-5393, various xpdf flaws (#345121)
- xdvi won't segfault if DVI file contains character which
  is not present in font (#243630)
- fix dvips -z buffer overflow with long href (#368591)
- fix insecure usage of temporary file in dviljk (#368611, #368641)
- link against poppler, not internal xpdf
- include arabtex

* Tue Oct 16 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.14
- xdvi won't segfault if DVI file contains character which
  is not present in font (#243630)

* Wed Sep 19 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.13
- update ls-Rs to deal with the japanese support
- update ptex to 3.1.10 and mendex to 2.6e
- fix install-info in scriptlets

* Tue Sep 18 2007 Patrice Dumas <pertusus@free.fr>
- subpackage packages that have a distinct upstream
- remove non free parts from the archive
- install xdvi icon in hicolor directory

* Thu Aug 30 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.12
- update description
- BR ruby, don't obsolete tetex-tex4ht
- remove license problematic/useless stuff, based on email from Karl Berry
- move vfont.sample to doc
- preserve timestamps
- shuffle binaries between texlive and texlive-fonts, update scriptlets

* Mon Aug 27 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.11
- BR gawk, ghostscript
- incorporate path fixes by Patrice Dumas
- change in the kpathsea default paths
- don't BR the *-texmf
- ship kpathsea defaults as documentation
- disable build of ps2eps at configuration time

* Wed Aug 22 2007 MATSUURA Takanori <t.matsuu at gmail.com> - 2007-0.10.1
- add Japanese pTeX
- Polish platex and pdfplatex are moved to platex-pl and
  pdfplatex respectively

* Sat Aug 18 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.10
- update License tag to licenses used in TeXLive sources
- remove ps2eps, it's a separate package
- don't remove updmap.cfg in post phase
- fix provides/obsoletes
- tetex.cron -> texlive.cron
- review fixes thanks to Patrice Dumas:
- remove .gz from installing info in scriptlets
- remove useless comments, lesstif/lesstif-devel requires
- remove X-Red-Hat-Extra category from xdvi.desktop
- update texlive-texdoc.patch
- require xdg-utils, htmlview, don't require bison, flex, ed

* Tue Aug 14 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.9
- update internal xpdf to 3.02 from upstream to fix CVE-2007-3387
- don't link statically with libstdc++
- put xdvi.xaw3d to texlive-xdvi instead of main package

* Tue Aug 07 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.8
- xdvi now compiles with Xaw3d support on i386

* Tue Jul 24 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.7
- obsolete tetex

* Wed Jul 18 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.6
- bump release to sync with texlive-texmf package changes

* Tue Jul 10 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.5
- separate kpathsea from texlive-fonts
- update filelists
- incorporate fixes from David Walluck (Mandriva, Debian, SuSE patches, etc.)
- link against system freetype2/t1lib
- remove kpathsea library building hacks
- disable ttf2pk, don't link against type1
- fix perl requires

* Tue Jun 26 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.4
- reintroduce the texlive-errata scheme
- update filelist
- cleanup patches

* Mon Jun 04 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.3
- use $TEXMFDOCS instead of $TEXMF/doc in texdoc (#232769)

* Fri Jun 01 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.2
- update to TeXLive 2007 final
- remove texlive-errata dependencies
- don't use dates in upstream tarball names
- fix invalid freetype libraries location
- disable broken parallel build
- move filelists back to the spec

* Mon Feb 12 2007 Jindrich Novy <jnovy@redhat.com> - 2007-0.1
- update to TeXLive 2007 rc

* Wed May 31 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.9
- missing BuildRequires added (desktop-file-utils) - doh!

* Tue May 30 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.8
- fixed some directory ownership issues.
- added icon for xdvi so I can install the desktop file

* Mon May 29 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.7
- first attempt at mock build (in fc5)

* Sun May 28 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.6
- ghost the texmf-var/web2c/*.{log,fmt,mem} files and create them
- during post install

* Sun May 28 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.5
- The main package needs to require the fonts package

* Sat May 27 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.4
- Patch 8 and Patch 19

* Sat May 27 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.3
- renamed to texjive

* Wed May 24 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.2
- apply Fedora/Red Hat patches (except fot japanese)
- port patches as needed
-- Some of the scripts not patched have same tmpdir issue as the
-- badscript patch fixes - so a second badscript patch IS still needed
- build shared libkpathsea

* Wed May 24 2006 Michael A. Peters <mpeters@mac.com> - 2005-0.1
- Initial attempt at something that resembles packaging.
-- Red Hat / Fedora specific patches from tetex not carried over yet
-- probably some regression
