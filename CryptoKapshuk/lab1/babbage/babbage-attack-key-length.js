let text = "Xsrrmlq pgui rrmq wel reb ozcb fcor qoil sr Nbmtox Bbmto. Lc geq dejv, xfsr yxh tovw ypb, tybqmlq fw dlc cmjfip yj fsw fkmp krb liybh, urmar acbi zyxf vslq ilyyer xm dyau mlds fsw zopr. Ri ukw uoepsre vslq vmliq, k tsbtjo gjyei glgml qgind xfo kpyyln eln lgql-foijoh, zegivib lsmdw. Fsw zvyc occc acbi jskfd, fpskfd eln wnkvivmlq fcrmln lyvj-kysl ctcmxympcc eln lgc rmci ukw tovw vslq eln gpysioh, yc xfyyer mr reb licx fpyocx er viycx rgmao. Xfsw kkrq xeko ayc Ejlyq Nyklpcnspo.";
let rawText = text.replace(/[!~@(\+)\{\}"'#`|\-\:\?$%^;, .<>&*0-9]/g, '').toLowerCase()
console.log(rawText);

F = (s, n) => {
  var G = (a, b) => b ? G(b, a % b) : a; // GCD function

  var p, w, i, j, f = 0; // f starting divisor
  for(i = 0; s[i + n - 1]; ++i) { // scan s for each substring of length n
     w = s.substr(i, n);
     for (j = i + n; (p = s.indexOf(w, j)) != -1; ++j) // find all occurencies of substring in the rest f the string
        f = G(p - i, f); // p-i is the distance between pairs
  }
  return +f
}

for(o = [], i = 1; i <= 10; i++) {
    o.push(i + '-' + F(rawText, i));
    console.log("i = " + i + ", F = " + F(rawText,i))
}

  console.log(o.filter(a => {
      let number = +a.split('-')[1]
      return number > 1
  }))