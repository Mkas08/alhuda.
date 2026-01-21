import {colors} from './colors';
import {typography} from './typography';
import {spacing} from './spacing';
import {borderRadius} from './borderRadius';

export const theme = {
  colors,
  typography,
  spacing,
  borderRadius,
  shadows: {
    sm: {
      shadowColor: '#000',
      shadowOffset: {width: 0, height: 1},
      shadowOpacity: 0.05,
      shadowRadius: 2,
      elevation: 1,
    },
    default: {
      shadowColor: '#000',
      shadowOffset: {width: 0, height: 4},
      shadowOpacity: 0.1,
      shadowRadius: 6,
      elevation: 3,
    },
    primaryGlow: {
      shadowColor: colors.primary.main,
      shadowOffset: {width: 0, height: 0},
      shadowOpacity: 0.3,
      shadowRadius: 15,
      elevation: 5,
    },
  },
};

export type Theme = typeof theme;
