$true = shift;
open(IN, $true);
while(<IN>){
    chomp $_;
    @s=split(/\s+/,$_);
    $truelabels{$s[1]}=$s[0];
}close IN;

$predict = shift;
open(IN,$predict);
while(<IN>){
        chomp $_; @s=split(/\s+/,$_);
        if(defined($truelabels{$s[1]})){
            $predictedlabels{$s[1]}=$s[0];
        }
        
}close IN;
$error=0;
foreach my $x (keys %predictedlabels){
    if($truelabels{$x} == 0 && $predictedlabels{$x} == 0) {$a++;}
    if($truelabels{$x} == 0 && $predictedlabels{$x} == 1) {$b++;}
    if($truelabels{$x} == 1 && $predictedlabels{$x} == 0) {$c++;}
    if($truelabels{$x} == 1 && $predictedlabels{$x} == 1) {$d++;}
}
$BER = 0.5*($b/($a+$b)+$c/($c+$d));
print "$BER\n";
