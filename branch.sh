#!/bin/sh
set -e
package=gcc
svn=svn://gcc.gnu.org/svn/$package
branch=branches/$package-6-branch
tag=tags/${package}_6_5_0_release
out=$package-branch.diff

# use filterdiff, etc to exclude bad chunks from diff
filter() {
	# remove revno's for smaller diffs
	sed -e 's,^\([-+]\{3\} .*\)\t(revision [0-9]\+)$,\1,'
}

old=$svn/$tag
new=$svn/$branch
echo >&2 "Running diff: $old -> $new"
LC_ALL=C svn diff -x --ignore-eol-style --force --old=$old --new=$new > $out.svn.tmp
filter < $out.svn.tmp > $out.tmp
rm -f $out.svn.tmp

if cmp -s $out{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f $out.tmp
	exit 0
fi
mv -f $out{.tmp,}

../md5 $package.spec
../dropin $out
