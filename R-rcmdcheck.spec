#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rcmdcheck
Version  : 1.4.0
Release  : 33
URL      : https://cran.r-project.org/src/contrib/rcmdcheck_1.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rcmdcheck_1.4.0.tar.gz
Summary  : Run 'R CMD check' from 'R' and Capture Results
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-callr
Requires: R-cli
Requires: R-curl
Requires: R-desc
Requires: R-digest
Requires: R-mockery
Requires: R-pkgbuild
Requires: R-prettyunits
Requires: R-rprojroot
Requires: R-sessioninfo
Requires: R-webfakes
Requires: R-withr
Requires: R-xopen
BuildRequires : R-R6
BuildRequires : R-callr
BuildRequires : R-cli
BuildRequires : R-curl
BuildRequires : R-desc
BuildRequires : R-digest
BuildRequires : R-mockery
BuildRequires : R-pkgbuild
BuildRequires : R-prettyunits
BuildRequires : R-rprojroot
BuildRequires : R-sessioninfo
BuildRequires : R-webfakes
BuildRequires : R-withr
BuildRequires : R-xopen
BuildRequires : buildreq-R

%description
of the individual checks. Supports running checks in the background,
    timeouts, pretty printing and comparing check results.

%prep
%setup -q -c -n rcmdcheck
cd %{_builddir}/rcmdcheck

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632788528

%install
export SOURCE_DATE_EPOCH=1632788528
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rcmdcheck
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rcmdcheck
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rcmdcheck
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rcmdcheck || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rcmdcheck/DESCRIPTION
/usr/lib64/R/library/rcmdcheck/INDEX
/usr/lib64/R/library/rcmdcheck/LICENSE
/usr/lib64/R/library/rcmdcheck/Meta/Rd.rds
/usr/lib64/R/library/rcmdcheck/Meta/features.rds
/usr/lib64/R/library/rcmdcheck/Meta/hsearch.rds
/usr/lib64/R/library/rcmdcheck/Meta/links.rds
/usr/lib64/R/library/rcmdcheck/Meta/nsInfo.rds
/usr/lib64/R/library/rcmdcheck/Meta/package.rds
/usr/lib64/R/library/rcmdcheck/NAMESPACE
/usr/lib64/R/library/rcmdcheck/NEWS.md
/usr/lib64/R/library/rcmdcheck/R/rcmdcheck
/usr/lib64/R/library/rcmdcheck/R/rcmdcheck.rdb
/usr/lib64/R/library/rcmdcheck/R/rcmdcheck.rdx
/usr/lib64/R/library/rcmdcheck/help/AnIndex
/usr/lib64/R/library/rcmdcheck/help/aliases.rds
/usr/lib64/R/library/rcmdcheck/help/paths.rds
/usr/lib64/R/library/rcmdcheck/help/rcmdcheck.rdb
/usr/lib64/R/library/rcmdcheck/help/rcmdcheck.rdx
/usr/lib64/R/library/rcmdcheck/html/00Index.html
/usr/lib64/R/library/rcmdcheck/html/R.css
/usr/lib64/R/library/rcmdcheck/tests/testthat.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/REDCapR-fail.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/REDCapR-ok.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/RSQLServer-install/00check.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/RSQLServer-install/00install.out
/usr/lib64/R/library/rcmdcheck/tests/testthat/_snaps/callback.md
/usr/lib64/R/library/rcmdcheck/tests/testthat/_snaps/comparison.md
/usr/lib64/R/library/rcmdcheck/tests/testthat/_snaps/parse.md
/usr/lib64/R/library/rcmdcheck/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/DESCRIPTION
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/NAMESPACE
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/R/package.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/man/foobar2.Rd
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/tests/testthat.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/tests/testthat/test-bad.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/tools/check.env
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad1/vignettes/test.Rmd
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad2/DESCRIPTION
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad2/NAMESPACE
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad2/R/package.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/DESCRIPTION
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/NAMESPACE
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/R/package.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/man/foobar2.Rd
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/tests/testthat.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/tests/testthat/test-bad.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad3/vignettes/test.Rmd
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad4/DESCRIPTION
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad4/NAMESPACE
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad4/R/package.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/bad4/man/foobar2.Rd
/usr/lib64/R/library/rcmdcheck/tests/testthat/bikedata-ok.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/dataonderivatives-test/00check.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/dataonderivatives-test/00install.out
/usr/lib64/R/library/rcmdcheck/tests/testthat/dataonderivatives-test/tests/testthat.Rout.fail
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/bad-tests.tar.gz
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/badenc.fail
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/badpackage_1.0.0.tar.gz
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/check_flavors.html
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/comparing.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/comparing2.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/r-devel-linux-x86_64-debian-clang/rcmdcheck-00check.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/r-devel-linux-x86_64-debian-gcc/rcmdcheck-00check.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/r-release-windows-ix86+x86_64/rcmdcheck-00check.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/checks/test-error.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/iso8859-15.rds
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/run1.rds
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/test-error.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/tests-as-cran.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/tests-not-as-cran.txt
/usr/lib64/R/library/rcmdcheck/tests/testthat/fixtures/win.rds
/usr/lib64/R/library/rcmdcheck/tests/testthat/helpers.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/minimal-ee.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/minimal-ewn.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/minimal-ok.log
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-auto_clean.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-build.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-callback.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-color.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-comparison.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-cran.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-crash.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-env.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-errors.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-http.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-parse.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-rcmdcheck.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-tests.R
/usr/lib64/R/library/rcmdcheck/tests/testthat/test-utils.R
