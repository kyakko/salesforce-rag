import { LightningElement, api } from 'lwc';

export default class ChatMessage extends LightningElement {
    @api message;

    get computedClass() {
        return this.message.author === 'user' ? 'user' : 'bot';
    }
}
