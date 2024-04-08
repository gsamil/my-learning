# Mel Frequency Cepstral Coefficient (MFCC) 

The shape of the vocal tract manifests itself in the envelope of the short time power spectrum, and the job of MFCCs is to accurately represent this envelope. 

Steps at a Glance  

- Frame the signal into short frames.
- For each frame calculate the periodogram estimate of the power spectrum. 
- Apply the mel filterbank to the power spectra, sum the energy in each filter. 
- Take the logarithm of all filterbank energies. 
- Take the DCT of the log filterbank energies. 
- Keep DCT coefficients 2-13, discard the rest. 

There are a few more things commonly done, sometimes the frame energy is appended to each feature vector. Delta and Delta-Delta features are usually also appended. Liftering is also commonly applied to the final features. 

## Why do we do these things?  

An audio signal is constantly changing, so to simplify things we assume that on short time scales the audio signal doesn't change much (statistically stationary). This is why we frame the signal into 20-40ms frames.  

The next step is to calculate the power spectrum of each frame. This is motivated by the human cochlea which vibrates at different spots depending on the frequency of the incoming sounds. Our periodogram estimate identifies which frequencies are present in the frame. 

The periodogram spectral estimate still contains a lot of information not required for ASR. In particular the cochlea can not discern the difference between two closely spaced frequencies. This effect becomes more pronounced as the frequencies increase. For this reason we take clumps of periodogram bins and sum them up to get an idea of how much energy exists in various frequency regions. This is performed by our Mel filterbank: the first filter is very narrow and gives an indication of how much energy exists near 0 Hertz. As the frequencies get higher our filters get wider as we become less concerned about variations. We are only interested in roughly how much energy occurs at each spot. The Mel scale tells us exactly how to space our filterbanks and how wide to make them. See below for how to calculate the spacing. 

 

Once we have the filterbank energies, we take the logarithm of them. This is also motivated by human hearing: we don't hear loudness on a linear scale. Generally to double the percieved volume of a sound we need to put 8 times as much energy into it. This means that large variations in energy may not sound all that different if the sound is loud to begin with. This compression operation makes our features match more closely what humans actually hear. Why the logarithm and not a cube root? The logarithm allows us to use cepstral mean subtraction, which is a channel normalisation technique. 

The final step is to compute the DCT of the log filterbank energies. There are 2 main reasons this is performed. Because our filterbanks are all overlapping, the filterbank energies are quite correlated with each other. The DCT decorrelates the energies which means diagonal covariance matrices can be used to model the features in e.g. a HMM classifier. But notice that only 12 of the 26 DCT coefficients are kept. This is because the higher DCT coefficients represent fast changes in the filterbank energies and it turns out that these fast changes actually degrade ASR performance, so we get a small improvement by dropping them. 

## What is the Mel scale?  

The Mel scale relates perceived frequency, or pitch, of a pure tone to its actual measured frequency. Humans are much better at discerning small changes in pitch at low frequencies than they are at high frequencies. Incorporating this scale makes our features match more closely what humans hear. 

The formula for converting from frequency to Mel scale is: 

$$M(f) = 1125~ln(1 + f/700)$$

To go from Mels back to frequency:

$$M^{-1}(m) = 700(exp(m/1125) - 1)$$

## References

- [Mel Frequency Cepstral Coefficient (MFCC) tutorial](http://practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)
