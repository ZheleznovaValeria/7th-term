let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
let position = alphabet.reduce((acc, val, index) => {
  acc[val] = index;
  //console.log(acc)
  //console.log(acc[val])
  return acc;
}, {});

let freq = [ 
  0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 
  0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 
  0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
  0.00978, 0.02360, 0.00150, 0.01974, 0.00074
];

function getMostLikely(count, len) {
  let min = Infinity, index = undefined;
  for (let offset = 0; offset < 26; offset++) {
    let deviation = 0;
    for (let i = 0; i < 26; i++) {
      const err = count[(i + offset) % 26] / len - freq[i];
      deviation += err * err;
    }
    if (deviation < min) {
      index = offset;
      min = deviation;
    }
  }
  return alphabet[index];
}

function getKey(ciphertext, keyLength) {
  let count = new Array(26).fill(0);
  let avg = new Array(26).fill(0);
  let key = '';
  
  for (let i = 0; i < keyLength; i++) {
    for (let j = i; j < ciphertext.length; j += keyLength) {
      count[ciphertext.charCodeAt(j) - 65]++;
    }
    
    key = key + getMostLikely(count, Math.floor((ciphertext.length - i) / keyLength));
    count.fill(0);
  }
  return key;
}

let text = 'xsrrmlqpguirrmqwelrebozcbfcorqoilsrnbmtoxbbmtolcgeqdejvxfsryxhtovwypbtybqmlqfwdlccmjfipyjfswfkmpkrbliybhurmaracbizyxfvslqilyyerxmdyaumldsfswzoprriukwuoepsrevslqvmliqktsbtjogjyeiglgmlqgindxfokpyylnelnlgqlfoijohzegiviblsmdwfswzvycocccacbijskfdfpskfdelnwnkvivmlqfcrmlnlyvjkyslctcmxympccelnlgcrmciukwtovwvslqelngpysiohycxfyyermrreblicxfpyocxerviycxrgmaoxfswkkrqxekoaycejlyqnyklpcnspo'.toUpperCase()
let keyLength = 3

let result = getKey(text, keyLength)
console.log(result)