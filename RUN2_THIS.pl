$mean = 0;
$data = shift;
$dir=$data;
for(my $i=0; $i<10; $i++){
  system("python try2.py $dir/$data.data $dir/$data.trainlabels.$i > ls_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels ls_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Least squares error = $mean ($sd)\n";

################################################################################

$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python hinge_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i > hl_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels hl_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
 
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Hinge error = $mean ($sd)\n";

