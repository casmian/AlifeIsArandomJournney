import React from 'react';
import { View, StyleSheet, StatusBar } from 'react-native';
import { Text } from 'react-native-paper';
import { moderateScale, verticalScale } from 'react-native-size-matters';

const StartScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#1a1a2e" />
      
      {/* Título Principal */}
      <View style={styles.titleContainer}>
        <Text style={styles.mainTitle}>A Life's</Text>
        <Text style={styles.subTitle}>Random Journey</Text>
      </View>
      
      {/* Subtítulo descriptivo */}
      <View style={styles.descriptionContainer}>
        <Text style={styles.description}>
          Un RPG donde no eliges quién eres.{'\n'}
          Solo vives lo que te toca.
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0f0f23',
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: moderateScale(20),
  },
  titleContainer: {
    alignItems: 'center',
    marginBottom: verticalScale(40),
  },
  mainTitle: {
    fontSize: moderateScale(42),
    fontWeight: '300',
    color: '#e6e6fa',
    textAlign: 'center',
    letterSpacing: 2,
    marginBottom: verticalScale(8),
    textShadowColor: 'rgba(230, 230, 250, 0.3)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  subTitle: {
    fontSize: moderateScale(28),
    fontWeight: '600',
    color: '#9d4edd',
    textAlign: 'center',
    letterSpacing: 1.5,
    textShadowColor: 'rgba(157, 78, 221, 0.4)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 3,
  },
  descriptionContainer: {
    marginTop: verticalScale(20),
    paddingHorizontal: moderateScale(30),
  },
  description: {
    fontSize: moderateScale(16),
    color: '#b3b3cc',
    textAlign: 'center',
    lineHeight: moderateScale(24),
    fontStyle: 'italic',
    opacity: 0.8,
  },
});

export default StartScreen; 