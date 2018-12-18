#!/usr/bin/perl

# Steven Woods
# Advent of Code 2018
# Day 4: Repose Record (Perl solution)
# To run: perl guards.pl <path/to/file>

use warnings;
use strict;

my ($file);
foreach my $input (@ARGV) {
  $file = $input;
}
my @data;
open(DATA, $file) or die "Error: Could not open file $file\n";
while (my $line = <DATA>) {
  chomp $line;
  push @data, $line;
}
close DATA;

@data = sort @data;

my %sleep_duration;
my %sleep_minutes;

my ($guard, $sleep_time, $wake_time);
foreach my $line (@data) {
  if ($line =~ /#/) {
    my @ary = split(/\s/, $line);
    foreach my $element (@ary) {
      if ($element =~ /#/) {
	$guard = $element;
#	print "\n", $guard, "\n";
      }
    }
  } else {
    my @ary = split(/:/, $line);
    @ary = split(/\]/,$ary[1]);
    my $time = $ary[0];
    if ($line =~ /sleep/) {
      $sleep_time = $time;
    } elsif ($line =~ /wake/) {
      $wake_time = $time;

      my $duration = $wake_time - $sleep_time;
#      print $guard, "\t", $duration, "\n";
      if ($sleep_duration{$guard}) {
	$sleep_duration{$guard} = $sleep_duration{$guard} + $duration;
      } else {
	$sleep_duration{$guard} = $duration;
      }

      while ($sleep_time < $wake_time) {
	push @{$sleep_minutes{$guard}}, $sleep_time;
	$sleep_time++;
      }

    }
  }
}

my ($sleepiest_guard, $max_sleep);
$max_sleep = 0;
foreach my $guard (keys %sleep_duration) {
  if ($sleep_duration{$guard} > $max_sleep) {
    $max_sleep = $sleep_duration{$guard};
    $sleepiest_guard = $guard;
  }
}
print "The sleepiest guard is Guard $sleepiest_guard. He slept for $max_sleep minutes.\n";

my %minute_count;
foreach my $minute (@{$sleep_minutes{$sleepiest_guard}}) {
  $minute_count{$minute}++;
}
my $sleepiest_minute;
my $count = 0;
foreach my $minute (keys %minute_count) {
  if ($minute_count{$minute} > $count) {
    $count = $minute_count{$minute};
    $sleepiest_minute = $minute;
  }
}

print "He was asleep most often at 00:$sleepiest_minute.\n";

my ($overall_sleepiest_minute, $second_sleepiest_minute, $second_sleepiest_guard);
my $overall_count = 0;
foreach my $guard (keys %sleep_minutes) {
  undef %minute_count;
  foreach my $minute (@{$sleep_minutes{$guard}}) {
    $minute_count{$minute}++;
  }
  my $count = 0;
  foreach my $minute (keys %minute_count) {
    if ($minute_count{$minute} > $count) {
      $count = $minute_count{$minute};
      $second_sleepiest_minute = $minute;
    }
  }
  if ($minute_count{$second_sleepiest_minute} > $overall_count) {
    $overall_count = $minute_count{$second_sleepiest_minute};
    $overall_sleepiest_minute = $second_sleepiest_minute;
    $second_sleepiest_guard = $guard;
  }
}

print "Guard $second_sleepiest_guard is most frequently asleep on the same minute. He was asleep at 00:$overall_sleepiest_minute a total of $overall_count times.\n";
