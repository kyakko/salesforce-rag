import { LightningElement, track } from 'lwc';

export default class ChatLauncher extends LightningElement {
    @track open = false;

    toggleWindow() {
        this.open = !this.open;
    }
}
