# Home Assistant Blinds Control Integration

Upgrade your Home Assistant with this custom blinds control integration. It's designed to effortlessly manage your time-based blinds, syncing with your chosen entities for raising and lowering. Plus, it remembers your settings after restarts and supports tilting.

## Acknowledgment

This is a fork of [Home Assistant Blinds Control Integration]() done by []().
Fork was based on and inspired by this insightful [community post](https://community.home-assistant.io/t/custom-component-cover-time-based/187654)

## Fork purpose

Focusing project on providing cover entity with only cover related functionality (exposing % open and commands). Additional features of original are removed and can be implemented separately by leveraging exposed cover entity.

## How to Install

Getting started is a piece of cake!

You can add this integration through HACS (Home Assistant Community Store) as a custom repository, or simply copy all files from the custom_components/blinds_controller directory into your Home Assistant's /custom_components/blinds_controller/ directory. 

Then, just give Home Assistant a quick restart, and you're good to go.

## Setting Things Up

Head over to Settings -> Devices and Services -> Click on Add Integration (select Blinds Control) to integrate your blinds into the system.

Name your blinds, select the controlling entities, specify roll-up and roll-down times in seconds, and if you need it, set tilt times (or leave them at 0 if you don't want to tilt support).

Once everything is set up, the calculations will indicate that the blinds are fully closed. Therefore, after configuring, <span style="color:red">wait</span> before submitting, roll your blinds down, and then submit.

You can also tweak existing configurations to suit your preferences (just reload the edited entries).

## Reporting issue and/or Contributing

I have forked project to use for my own needs, and don't have significant amount of time to invest in this project. You may create [issues](https://github.com/vilaemail/BUT_blinds_time_control/issues), but I am not sure when and if I could address them.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/MatthewOnTour/BUT_blinds_time_control?tab=MIT-1-ov-file) file for details.

