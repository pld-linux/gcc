#!/usr/bin/perl

sub trim
{
    my $string = shift;
    $string =~ s/^\s+//;
    $string =~ s/\s+$//;
    return $string;
}

open(F, $ARGV[0]) or die("cannot open file: $ARGV[0]\n");
@lines = <F>;
close(F);

@deps = ();

foreach (@lines)
{
    if (/(^dependency_libs='(.*)')[\ \t]*$/)
    {
	my $trimmed = trim($2);
	$trimmed =~ y/'//d;
	@libs = split(/[\ \t\n]+/, $trimmed);
	@L = grep(/^-L.*gcc\/.*\/\d\.\d\.\d(\/(32|64|x32|nof))*$/, @libs);
	@l = grep(/^(-l.*|\/.*\.la$)/, @libs);
	$opt_L = join(' ', @L);
	$opt_l = join(' ', @l);
	print("dependency_libs='");
	print($opt_L);
	if (scalar(@L))
	{
	    print(" ");
	}
	print($opt_l);
	print("'\n");
    }
    elsif (/^libdir='(.*)'/)
    {
	print("libdir='$ARGV[1]'\n");
    }
    else
    {
	print($_);
    }
}
