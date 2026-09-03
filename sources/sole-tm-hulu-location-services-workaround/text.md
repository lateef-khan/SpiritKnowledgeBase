# Hulu Location Services Workaround - Treadmills

Step transcript of the video file `Hulu Location Services Workaround - Treadmills.mp4`.

## How this transcript was made

The video is 43 seconds long, 1920x1080, and **silent** — its audio track measures a mean volume of -48.8 dB with no speech. There is no narration. This transcript was reconstructed by extracting frames and reading the console screen in each one.

Because the video is silent, it shows **what to tap** but never says **why**. It gives no symptom description, no error message, and no explanation of the underlying cause. Do not infer one.

The machine shown is a touchscreen treadmill with INCLINE and SPEED key columns, a GARMIN button in the top bar, and the Guest profile logged in.

## Observed steps, with timestamps

| Time | Screen |
|---|---|
| 0s | Console home screen, "Hello, Guest". Top bar: GARMIN, and icons for heart rate, Bluetooth, gear, profile. Wi-Fi symbol at the top right. |
| 2s | Finger taps the **Wi-Fi symbol in the top right corner**. |
| 4s | The Android **Wi-Fi** settings page opens. "Use Wi-Fi" is on, "SoleWifi Connected" at the top of the network list. |
| 8-9s | Finger taps the **magnifying glass in the top right of the Wi-Fi page**. |
| 10s | An Android settings **Search** screen opens, with an empty "Search..." field and an on-screen keyboard. Recent searches shown: location, system, developer. |
| 12-18s | Types `location` one letter at a time. Interim results include Location, Logging level, Logger buffer sizes, Location services for work, Pointer location. |
| 20s | Taps the first **Location** result (breadcrumb `null > Location`). |
| 22s | The **Location** settings page opens. **"Use location" is already on.** "Recent location requests: No apps have requested location recently". "Wi-Fi and Bluetooth scanning: **Both Wi-Fi and Bluetooth scanning are off**". |
| 24s | "App permission: 9 of 10 apps have access to location". Finger moves to **Wi-Fi and Bluetooth scanning**. |
| 26-28s | The **Wi-Fi and Bluetooth scanning** page opens. Two toggles, **both off**: "Wi-Fi scanning - Allow apps and services to scan for Wi-Fi networks at any time, even when Wi-Fi is off" and "Bluetooth scanning - Allow apps and services to scan for nearby devices at any time, even when Bluetooth is off". |
| 30s | **Both toggles are now on.** |
| 32s | Back on the Location page. It now reads "Wi-Fi and Bluetooth scanning: **Both Wi-Fi and Bluetooth scanning are on**". |
| 34s | Taps **App permission**. The page shows "Loading...". |
| 36s | The **Location** permission list opens. ALLOWED ALL THE TIME: `AC00551-56T-09`, Google Play Store. ALLOWED ONLY WHILE IN USE: Chrome, ESPN, Hulu, Kinomap, Peacock, Prime Video. |
| 38-40s | Taps **Hulu**. The **Location permission** page for Hulu shows "LOCATION ACCESS FOR THIS APP" with two choices: **Allow only while using the app** (selected) and **Deny**. A "See all Hulu permissions" link sits below. |
| 42s | Back on the Location permission list. Hulu is under ALLOWED ONLY WHILE IN USE. |

## Navigation overlay

Throughout the video a small floating panel sits on top of the screen with three buttons: **Apps**, **Go Back**, and **Show Panels** / **Hide Panels**. It is used to go back out of Android settings screens, and it is dragged around the screen to uncover controls hidden behind it.
