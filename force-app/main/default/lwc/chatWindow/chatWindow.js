import { LightningElement, track } from 'lwc';
import { sendMessage } from 'c/chatService';

export default class ChatWindow extends LightningElement {
    @track messages = [];
    @track input = '';
    @track loading = false;

    handleChange(event) {
        this.input = event.target.value;
    }

    handleKeyPress(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            this.send();
        }
    }

    async send() {
        const text = this.input.trim();
        if (!text) {
            return;
        }
        this.messages = [
            ...this.messages,
            { id: Date.now(), author: 'user', text }
        ];
        this.input = '';
        this.loading = true;
        try {
            const data = await sendMessage(text);
            this.messages = [
                ...this.messages,
                { id: Date.now() + 1, author: 'bot', text: data.answer }
            ];
        } catch (e) {
            this.messages = [
                ...this.messages,
                { id: Date.now() + 1, author: 'bot', text: 'Error contacting server' }
            ];
        } finally {
            this.loading = false;
        }
    }

    close() {
        this.dispatchEvent(new CustomEvent('close'));
    }
}
