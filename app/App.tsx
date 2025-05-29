import React from 'react';
import { Provider as PaperProvider } from 'react-native-paper';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import StartScreen from './src/screens/StartScreen';

export default function App() {
  return (
    <SafeAreaProvider>
      <PaperProvider>
        <StartScreen />
      </PaperProvider>
    </SafeAreaProvider>
  );
} 