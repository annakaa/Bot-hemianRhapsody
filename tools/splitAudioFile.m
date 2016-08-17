function splitAudioFile(infile, outdir, Fs, fromS, toS, index)





[samples channels] = wavread(infile, 'size');



  infile
  startSamp = Fs*(fromS-3);
  startSamp = max(startSamp,0);
  endSamp = Fs*(toS+3);
  endSamp = min(endSamp, samples);
  currentData = wavread(infile, [startSamp endSamp]);
  rampUp = 0:1/(Fs*3):1;
  rampDown = 1:-1/(Fs*3):0;
  ramp1 = rampUp*currentData(1:Fs*3);
  ramp2 = rampDown*currentData(end-Fs*3:end);
  currentData = [ramp1 currentData(Fs*3:end-Fs*3) ramp2];
  outname = [outdir '/' infile(1:end-4) '_' num2str(index) '.wav'];
  wavwrite(currentData, Fs, outname);
end
