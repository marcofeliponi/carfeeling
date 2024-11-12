<template>
    <div>
        <header class="title">
            <h2>{{ targetCar }}</h2>
        </header>
        <div class="chat">
            <div v-for="message in messages" :key="message.id" class="messages">
                <div v-if="message.role === 'assistant'" class="message-box">
                    <span style="align-self: flex-start; margin-left: 5px; font-weight: bold;">Inteligência
                        Artificial</span>
                    <span class="ai-message">{{ message.content }}</span>
                </div>
                <div v-if="message.role === 'user'" class="message-box">
                    <span style="align-self: flex-end; margin-right: 7px; font-weight: bold;">Você</span>
                    <span class="user-message">{{ message.content }}</span>
                </div>
            </div>
            <div v-if="aiTyping" class="ai-typing">
                . . .
            </div>
        </div>
        <footer class="input-container">
            <div class="input">
                <NConfigProvider :themeOverrides="theme">
                    <n-space vertical>
                        <n-input ref="inputChatRef" :maxlength="150" :disabled="aiTyping" size="large" round
                            placeholder="Faça uma pergunta" v-model:value="inputText"
                            v-on:keyup.enter="sendChat(inputText)" />
                    </n-space>
                </NConfigProvider>
            </div>
        </footer>
    </div>
</template>

<script>
import { NInput, NSpace, NConfigProvider } from 'naive-ui';
import axios from 'axios';

export default {
    name: 'AiChat',

    data() {
        return {
            aiTyping: false,
            targetCar: `${this.$route.query.brand} ${this.$route.query.model} ${this.$route.query.year}`,
            inputText: '',
            theme: {
                common: {
                    primaryColor: '#14213D',
                    primaryColorHover: '#14213D',
                    primaryColorPressed: '#14213D',
                }
            },
            messages: [
                {
                    role: 'user',
                    content: `Olá, quais são os pontos positivos e negativos do veículo ${this.$route.query.brand} ${this.$route.query.model} ${this.$route.query.year}?`
                }
            ]
        }
    },

    components: {
        NInput,
        NSpace,
        NConfigProvider,
    },

    mounted() {
        this.sendChat();
    },

    methods: {
        async sendChat(message) {
            this.inputText = '';
            this.aiTyping = true;

            if (message) this.messages.push({ role: 'user', content: message });

            const response = await axios.post(`${import.meta.env.VITE_API_URL}/ai-chat/`, {
                messages: this.messages
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: this.$store.state.userToken
                }
            }
            ).catch(err => {
                console.error('Erro ao conversar com GPT', err);
            });

            const aiMessage = response.data.choices[0].message;
            this.messages.push(aiMessage);

            this.aiTyping = false;
        }
    }
}

</script>

<style scope lang="scss">
.title {
    color: black;
    display: flex;
    justify-content: center;
    font-family: 'Montserrat', sans-serif;
}

.chat {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px;
    overflow-y: auto;
    color: black;
    font-family: 'Lato', sans-serif;
    margin-bottom: 30px;

    .messages {
        overflow-y: auto;

        .message-box {
            display: flex;
            flex-direction: column;

            .user-message,
            .ai-message {
                background-color: var(--third-color);
                padding: 10px;
                border-radius: 10px;
                max-width: 50%;
                word-wrap: break-word;
                white-space: pre-line;
            }

            .ai-message {
                align-self: flex-start;
            }

            .user-message {
                align-self: flex-end;
            }
        }
    }

    .ai-typing {
        align-self: flex-start;
        font-weight: bold;
        margin-left: 5px;
        font-size: 25px;
        animation: typing 1s infinite;

        @keyframes typing {
            0% {
                opacity: 0;
            }

            50% {
                opacity: 1;
            }

            100% {
                opacity: 0;
            }
        }
    }
}

.input-container {
    position: fixed;
    width: 100%;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: var(--third-color);
    box-sizing: border-box;

    .input {
        width: 65%;
        padding: 10px;
        margin: 0 auto;
    }
}
</style>
