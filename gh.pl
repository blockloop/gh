#!/usr/bin/env perl

my $open_cmd;
my $platform = $^O;
if    ($platform =~ /linux/i)   { $open_cmd = "xdg-open"; }
elsif ($platform =~ /darwin/i)  { $open_cmd = "open"; }
elsif ($platform =~ /MSWin32/i) { $open_cmd = "start"; }
else                            { die "unknown platform: $platform\n"; }

my $remote = `git --no-optional-locks remote get-url origin` || die "\n";
if ($remote eq '') { die "Not a git repository or no origin URL\n"; }

my $branch = `git --no-optional-locks rev-parse --abbrev-ref HEAD` || die "\n";
$branch =~ s|\s||g;

my $suffix;
if ("$branch" ne 'master') {
        if    ($remote =~ /github\./i)    { $suffix = "/tree/$branch"; }
        elsif ($remote =~ /gitlab\./i)    { $suffix = "/tree/$branch"; }
        elsif ($remote =~ /bitbucket\./i) { $suffix = "/branch/$branch"; }
        elsif ($remote =~ /blockloop\./i) { $suffix = "/src/branch/$branch"; } # my gitea
}

# The URI package won't parse remotes without a scheme
$remote =~ s|^git@|ssh://git@|;

use URI;
my $uri  = URI->new($remote);
my $path = $uri->path;
my $host = $uri->host;
$host =~ s|:|/|;
$path =~ s|.git$||;

system("$open_cmd 'https://$host$path$suffix'");
