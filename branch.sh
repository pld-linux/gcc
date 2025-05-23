#!/bin/sh
set -e
url=git://gcc.gnu.org/git/gcc.git
package=gcc
tag=releases/gcc-14.3.0
branch=releases/gcc-14
out=$package-branch.diff
repo=$package.git

# use filterdiff, etc to exclude bad chunks from diff
filter() {
	cat
}

if [ ! -d $repo ]; then
	git clone --bare $url -b $branch $repo
fi

cd $repo
	git fetch origin +$branch:$branch +refs/tags/$tag:refs/tags/$tag
	git log -p --reverse $tag..$branch ":(exclude)doc/doc-*" ":(exclude)test" ":(exclude).*" | filter > ../$out.tmp
cd ..

if cmp -s $out{,.tmp}; then
	echo >&2 "No new diffs..."
	rm -f $out.tmp
	exit 0
fi
mv -f $out{.tmp,}

../md5 $package.spec
../dropin $out
