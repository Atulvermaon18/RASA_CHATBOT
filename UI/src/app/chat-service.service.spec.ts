import { TestBed } from '@angular/core/testing';

import { ChatServiceService } from './chat-service.service';

describe('ChatServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ChatServiceService = TestBed.get(ChatServiceService);
    expect(service).toBeTruthy();
  });
});
