// From: https://community.home-assistant.io/t/material-dark-theme/30796

var head = document.head || document.getElementsByTagName('head')[0];
var style = document.createElement('style');

style.type = 'text/css';

var css = ` html {
    --light_green: #08a8a5;
    --dark_green: #017775;
    --dark_grey: #232326;
    --light_grey: #344249;
    --red: #d10404;
    --yellow: #fffa0c;
    --white: #f7f7f7;

    --primary-color: var(--light_green);
    --light-primary-color: var(--red);
    --dark-primary-color: var(--red);
    --text-primary-color: var(--red);
    --primary-background-color: var(--dark_grey);
    --sidebar-text_-_background: var(--red);
    --paper-card-background-color: var(--light_grey);
    --paper-card-header-color: var(--white);
    --secondary-background-color: var(--dark_grey);
    --primary-text-color: var(--white);
    --secondary-text-color: var(--white);
    --paper-listbox-background-color: var(--light_grey);
    --paper-toggle-button-checked-ink-color: var(--red);
    --paper-toggle-button-checked-button-color: var(--yellow);
    --paper-toggle-button-checked-bar-color: var(--yellow);
    --paper-slider-knob-color: var(--yellow);
    --paper-slider-knob-start-color: var(--red);
    --paper-slider-pin-color: var(--red);
    --paper-slider-active-color: var(--yellow);
    --paper-slider-secondary-color: var(--red);
    --paper-slider-container-color: var(--red);
    --paper-progress-secondary-color: var(--red);
    --paper-item-selected_-_background-color: var(--light_green);
    --paper-item-icon_-_color: var(--red);
    --paper-item-icon-color: var(--dark_green);
    --paper-item-icon-active-color: var(--yellow);
    --paper-grey-50: var(--light_green);
    --paper-grey-200: var(--dark_green);
    --label-badge-background-color: var(--light_grey);
    --label-badge-text-color: var(--white);
    --label-badge-red: var(--red);
    --label-badge-blue: var(--red);
    --label-badge-green: var(--red);
    --label-badge-yellow: var(--red);
    --label-badge-grey: var(--red);
    --table-row-background-color: var(--light_grey);
    --table-row-alternative-background-color: var(--dark_grey);
}`;

style.appendChild(document.createTextNode(css));

head.appendChild(style);
